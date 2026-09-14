import sys
import requests

BOT_TOKEN = "8987520681:AAFrOKiD-Xep_IjygKa6bXhlH30el6Z-g6M"
CHAT_ID = "6740940338"


def send_telegram_message(text: str) -> bool:
    if "YOUR_BOT_TOKEN" in BOT_TOKEN or "YOUR_CHAT_ID" in CHAT_ID:
        print("[ERROR] Please replace BOT_TOKEN and CHAT_ID with your actual Telegram credentials.")
        return False

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        res_data = response.json()
        if response.status_code == 200 and res_data.get("ok"):
            print("[SUCCESS] Notification sent to Telegram successfully.")
            return True
        else:
            print(f"[FAILED] Telegram API Error: {res_data.get('description')}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network error contacting Telegram: {e}")
        return False


if __name__ == "__main__":
    msg = (
        "🚨 *Hermes Agent Alert*\n\n"
        "📦 *Event:* Low Stock Detected\n"
        "👗 *Item:* Linen Summer Abaya\n"
        "⚠️ *Remaining:* Only 4 units!\n"
        "📄 *Action:* Restock PO generated."
    )
    send_telegram_message(msg)