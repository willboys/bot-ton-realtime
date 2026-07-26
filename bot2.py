import os
import asyncio
import requests
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Bot

TOKEN = "7581064589:AAH-y6s4CyvmpTM3X3S0hnzuPGyHc4x8eI"
CHAT_ID = "-1003771467296"

bot = Bot(TOKEN)

last_price = None


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Running")


def web():
    port = int(os.environ.get("PORT", 10000))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()


async def main():
    global last_price

    while True:
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=idr,usd,rub"

            data = requests.get(url, timeout=20).json()

            idr = data["the-open-network"]["idr"]
            usd = data["the-open-network"]["usd"]
            rub = data["the-open-network"]["rub"]

            if last_price is None:
                last_price = idr

            if idr > last_price:
                emoji = "🟢"
                percent = ((idr-last_price)/last_price)*100
            elif idr < last_price:
                emoji = "🔴"
                percent = ((last_price-idr)/last_price)*100
            else:
                emoji = "⚪"
                percent = 0

            text = f"""✅ PRICE 1 TONCOIN NOW

📊 {emoji} {percent:.2f}%

🇮🇩 IDR : Rp{idr:,.0f}
🇺🇸 USD : ${usd:.2f}
🇷🇺 RUB : ₽{rub:.2f}

━━━━━━━━━━━━━━
CHANNEL OWNED BY
@ledaak
"""

            await bot.send_message(chat_id=CHAT_ID, text=text)

            last_price = idr

        except Exception as e:
            print(e)

        await asyncio.sleep(60)


threading.Thread(target=web, daemon=True).start()

asyncio.run(main())
