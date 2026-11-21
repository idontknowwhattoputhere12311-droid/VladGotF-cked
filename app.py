import os,json,gzip,time
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
frames=[f.encode('utf-8') for f in json.load(gzip.open('frames.json.gz','rt',encoding='utf-8'))]
class H(BaseHTTPRequestHandler):
 def do_GET(self):
  self.send_response(200);self.end_headers()
  try:
   self.wfile.write(b'\033[2J')
   while True:
    for f in frames: self.wfile.write(f);self.wfile.flush();time.sleep(0.08)
  except: pass
 def log_message(self,*a): pass
ThreadingHTTPServer(('0.0.0.0',int(os.environ.get('PORT',8080))),H).serve_forever()
