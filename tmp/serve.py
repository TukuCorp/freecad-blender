import http.server, os, sys
os.chdir('C:/Users/tukum/Downloads/freecad-blender')
port=int(open('tmp/server_port.txt').read().strip())
handler=http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(('', port), handler) as httpd:
    print(f"serving on {port}", flush=True)
    httpd.serve_forever()
