import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

port = int(os.environ.get('PORT', 3000))
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', port), handler)
print(f'Serving at port {port}')
httpd.serve_forever()
