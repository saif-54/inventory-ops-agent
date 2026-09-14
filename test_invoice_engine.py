from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = "C:/Users/saifh/agent_workspace/order_invoice.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
story = []
styles = getSampleStyleSheet()

# Header
title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=20, leading=24, textColor=colors.HexColor("#1A1A1A"))
story.append(Paragraph("<b>ABAYA COUTURE - ORDER INVOICE</b>", title_style))
story.append(Paragraph("Order ID: #ORD-9842 | Date: 2026-09-14", styles['Normal']))
story.append(Spacer(1, 15))

# Order Table Data
data = [
    ["SKU", "Item Description", "Qty", "Unit Price", "Total"],
    ["ABY-001", "Classic Crepe Abaya (Size 56)", "2", "950 EGP", "1,900 EGP"],
    ["ABY-003", "Silk Embroidered Kaftan (Size 58)", "1", "1,400 EGP", "1,400 EGP"],
    ["", "", "", "Subtotal:", "3,300 EGP"],
    ["", "", "", "Shipping:", "60 EGP"],
    ["", "", "", "Total Due:", "3,360 EGP"]
]

table = Table(data, colWidths=[80, 240, 50, 80, 85])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2C2C2C")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('ALIGN', (1, 0), (1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('GRID', (0, 0), (-1, -4), 0.5, colors.grey),
    ('LINEABOVE', (3, 3), (-1, -1), 1, colors.black),
    ('FONTNAME', (3, 3), (-1, -1), 'Helvetica-Bold'),
]))

story.append(table)
doc.build(story)

print(f"\n--- PDF Invoice Generated Successfully ---\nFile saved at: {pdf_path}\n")