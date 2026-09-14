import argparse
import os
import sqlite3
import sys
import requests
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

DB_PATH = "C:/Users/saifh/agent_workspace/abaya_inventory.db"
RESTOCK_PDF = "C:/Users/saifh/agent_workspace/restock_purchase_order.pdf"
WEBHOOK_URL = "https://httpbin.org/post"


def run_pipeline(dry_run=False):
    print("\n==================================================")
    print("   HERMES AGENT: INTEGRATED E-COMMERCE PIPELINE   ")
    print("==================================================")

    if not os.path.exists(DB_PATH):
        print(f"[CRITICAL] Database not found at: {DB_PATH}")
        sys.exit(1)

    # 1. Inspect Inventory for Low Stock
    print("\n[Phase 1] Scanning SQLite Inventory for Low Stock (Threshold <= 5)...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT sku, name, fabric, stock, cost FROM products WHERE stock <= 5")
    low_stock_items = cursor.fetchall()
    conn.close()

    if not low_stock_items:
        print("  -> All items adequately stocked. No restock needed.")
        return

    print(f"  -> Found {len(low_stock_items)} item(s) requiring immediate restock:")
    for item in low_stock_items:
        print(f"     * [{item[0]}] {item[1]} (Stock: {item[3]}, Cost: {item[4]} EGP)")

    # 2. Generate Restock Purchase Order PDF
    print("\n[Phase 2] Generating Restock Purchase Order (ReportLab Engine)...")
    doc = SimpleDocTemplate(RESTOCK_PDF, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []
    styles = getSampleStyleSheet()

    header_style = ParagraphStyle('Header', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor("#1A1A1A"))
    story.append(Paragraph("<b>RESTOCK PURCHASE ORDER (URGENT)</b>", header_style))
    story.append(Paragraph("Generated Automatically by Hermes Agent Workspace", styles['Normal']))
    story.append(Spacer(1, 15))

    table_data = [["SKU", "Item Description", "Fabric", "Current Stock", "Order Qty"]]
    for item in low_stock_items:
        table_data.append([item[0], item[1], item[2], str(item[3]), "50 Units"])

    po_table = Table(table_data, colWidths=[80, 200, 100, 80, 80])
    po_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#333333")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(po_table)
    doc.build(story)
    print(f"  -> Restock PDF generated successfully: {RESTOCK_PDF}")

    # 3. Dispatch Outbound Alert Webhook
    print("\n[Phase 3] Dispatching Alert Notification via Webhook...")
    if dry_run:
        print("  -> DRY RUN enabled: Skipping external network request.")
    else:
        payload = {
            "source": "Hermes Master Pipeline",
            "alert": "Restock Order Generated",
            "items_affected": [item[1] for item in low_stock_items],
            "document": "restock_purchase_order.pdf"
        }
        try:
            res = requests.post(WEBHOOK_URL, json=payload, timeout=8)
            print(f"  -> Notification Delivered! Status: {res.status_code} OK")
        except requests.exceptions.RequestException as err:
            print(f"  -> Webhook notification failed: {err}")

    print("\n==================================================")
    print("       PIPELINE EXECUTION COMPLETED SUCCESSFULLY  ")
    print("==================================================\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hermes Agent Operations Runner")
    parser.add_argument("--dry-run", action="store_true", help="Run without sending webhooks")
    args = parser.parse_args()
    run_pipeline(dry_run=args.dry_run)