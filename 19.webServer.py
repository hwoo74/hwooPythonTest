import threading
from http.server import ThreadingHTTPServer, CGIHTTPRequestHandler

def webSvr1(port : int, server_class=ThreadingHTTPServer, handler_class=CGIHTTPRequestHandler):
    server_address = ('', port)
    handler_class.cgi_directories = ['./cgi-http']

    print("serving at port", port)

    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

# http://localhost:8080/cgi-http/test.py
# 위 주소 접속시 test.py 실행.


import http.server
import socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<b>Hello Sidney,</b>")
        elif self.path == '/sidney':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<font color=\"red\">My name is Sideny</font>")
        else:
            self.send_error(404)

def webSvr2( PORT ) :
    #Handler = http.server.SimpleHTTPRequestHandler
    Handler = MyHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()



if __name__ == "__main__":
    threading.Thread(target=webSvr1, args=(8080, )).start()
    threading.Thread(target=webSvr2, args=(8081, )).start()
