import http.server
import os

os.chdir('/Users/fedorkrasnov/Desktop/port')

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(('', 3000), handler)
print('Serving at port 3000')
httpd.serve_forever()
