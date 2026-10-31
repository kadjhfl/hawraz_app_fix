from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import socket
import threading
import time
import webbrowser

ROOT = Path(__file__).resolve().parent
PREFERRED_PORT = 8765

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        print('[HAWRAZ] ' + (fmt % args))

def choose_server():
    # Prefer the stable origin so an existing local IndexedDB database can remain
    # associated with the same origin when the same port/root is reused.
    for port in (PREFERRED_PORT, 8766, 8767, 8768, 8769, 8770):
        try:
            server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
            return server, port
        except OSError:
            continue
    raise RuntimeError('پورت آزاد برای اجرای برنامه پیدا نشد. پنجره‌های قبلی سرور HAWRAZ را ببند و دوباره تلاش کن.')

server, port = choose_server()
url = f'http://127.0.0.1:{port}/index.html'
print('HAWRAZ is running locally: ' + url)
print('برای بستن برنامه، همین پنجره را ببند یا Ctrl+C بزن.')
threading.Timer(1.0, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    print('\nHAWRAZ server stopped.')
finally:
    server.server_close()
