import os
import time
import json
import urllib.request
import urllib.parse
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

TOKEN = "7581064589:AAH-y6s4CyvmpTM3X3S0hnzuPGyHc4x8eI"
CHAT_ID = "-1003771467296"
last_price = None

# 1. Server web HTTP agar Render menganggap layanan aktif (Live)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Running OK")

def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

# 2. Fungsi pengirim pesan langsung via API Telegram (HTTP POST murni)
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'Markdown'
    }).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read()
    except Exception as e:
        print("Telegram API Error:", e)

# 3. Loop utama bot pengambil harga crypto
def run_bot():
    global last_price
    print("Direct HTTP Telegram Bot started...")
    time.sleep(3)
    
    while True:
        try:
            # Ambil data dari CoinGecko
            api_url = "https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=idr,usd,rub"
            req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
            
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

            # Kirim pesan langsung
            send_telegram_message(text)
            last_price = idr
            print("Price update sent successfully!")

        except Exception as e:
            print("Main Loop Error:", e)

        # Jeda 60 detik
        time.sleep(60)

if __name__ == "__main__":
    # Jalankan server web di background thread
    threading.Thread(target=run_web, daemon=True).start()
    
    # Jalankan bot di thread utama
    run_bot()
