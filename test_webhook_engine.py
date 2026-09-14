import json
import requests

# Simulated Webhook Endpoint (httpbin echoes back posted payloads securely)
webhook_url = "https://httpbin.org/post"

# Payload: Low stock alert from abaya inventory
payload = {
    "event": "inventory_alert",
    "brand": "Abaya Couture",
    "timestamp": "2026-09-14T21:15:00Z",
    "product": {
        "sku": "ABY-002",
        "name": "Linen Summer Abaya",
        "stock_remaining": 4,
        "action_required": "Restock Urgently"
    }
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Hermes-Automation-Agent/1.0"
}

print("\n--- Dispatching Outbound Alert Webhook ---")
try:
    response = requests.post(webhook_url, json=payload, headers=headers, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        print(f"[SUCCESS] Status Code: {response.status_code} OK")
        print(f"Server Acknowledged: Event '{data['json']['event']}' received.")
        print(f"Alert Dispatched For: {data['json']['product']['name']} (Stock: {data['json']['product']['stock_remaining']})")
    else:
        print(f"[WARNING] Server responded with code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"[ERROR] Webhook connection failed: {e}")

print("\nWebhook engine verified successfully.\n")