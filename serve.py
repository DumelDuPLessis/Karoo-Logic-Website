"""Simple static file server — run with: python serve.py"""
import http.server
import socketserver
import os

PORT = 3000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({'.js': 'application/javascript', '.mjs': 'application/javascript'})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
