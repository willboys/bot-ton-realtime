import time
import json
import urllib.request
from telegram import Bot

TOKEN = "7581064589:AAH-y6s4CyvmpTM3X3S0hnzuPGyHc4x8eI"
CHAT_ID = "-1003771467296"

bot = Bot(TOKEN)
last_price = None

def main():
    global last_price
    print("Bot started...")
    while True:
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=idr,usd,rub"
            
            # Menggunakan urllib bawaan Python murni (tidak butuh requests sama sekali)
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as response:
                data = json.loads(response.read().decode())
            
            idr = data["the-open-network"]["idr"]
            usd = data["the-open-network"]["usd"]
            rub = data["the-open-network"]["rub"]

            if last_price is None:
                last_price = idr

            if idr > last_price:
                emoji = "🟢"
                percent = ((idr - last_price) / last_price) * 100
            elif idr < last_price:
                emoji = "🔴"
                percent = ((last_price - idr) / last_price) * 100
            else:
                emoji = "⚪"
                percent = 0.0

            text = f"""✅ **PRICE 1 TONCOIN NOW**

📊 {emoji} {percent:.2f}%

🇮🇩 IDR : Rp{idr:,}
🇺🇸 USD : ${usd}
🇷🇺 RUB : ₽{rub}"""

            # Menggunakan perintah sync agar kompatibel di semua versi telegram-bot
            bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")
            last_price = idr

        except Exception as e:
            print("Error:", e)

        time.sleep(60)

if __name__ == "__main__":
    main()
