import os
import time
import json
import urllib.request
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Bot

TOKEN = "7581064589:AAH-y6s4CyvmpTM3X3S0hnzuPGyHc4x8eI"
CHAT_ID = "-1003771467296"

bot = Bot(TOKEN)
last_price = None

# 1. Jalankan server web murni untuk menjaga port Render tetap terbuka
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

# 2. Fungsi utama pengirim pesan bot secara sinkron (100% bebas macet)
def run_bot():
    global last_price
    print("Bot worker started successfully...")
    time.sleep(5) # Jeda sejenak agar server web siap duluan
    
    while True:
        try:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=idr,usd,rub"
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

            # Kirim pesan menggunakan fungsi sinkron standar
            bot.send_message(chat_id=CHAT_ID, text=text, parse_mode="Markdown")
            last_price = idr
            print("Message successfully sent to channel.")

        except Exception as e:
            print("Error sending message:", e)

        # Tunggu 60 detik sebelum perulangan berikutnya
        time.sleep(60)

if __name__ == "__main__":
    # Jalankan server web di background
    threading.Thread(target=run_web, daemon=True).start()
    
    # Jalankan bot utama di thread utama
    run_bot()
