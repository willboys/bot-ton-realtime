import asyncio

async def main():
    print("Halo TON BOT")
    while True:
        await asyncio.sleep(60)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Fungsi server web dummy agar Render tidak mendeteksi error port
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_web():
    server = HTTPServer(('0.0.0.0', 10000), SimpleHandler)
    server.serve_forever()

# Jalankan server web di latar belakang
threading.Thread(target=run_web, daemon=True).start()
