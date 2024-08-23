from http.server import BaseHTTPRequestHandler, HTTPServer
req = None

class RequestHandler_httpd(BaseHTTPRequestHandler) :
    def do_GET(self):
        global req
        req = self.requestline
        req = req[5 : int(len(req) - 9)]
        req = req.replace("%20"," ")
        print('You received a request')
        f = open("variable.txt", "w")
        f.write(req)
        f.close()
        print(req)
        r = open("response.txt", "r+")
        messagetosend = bytes(r.read(), "utf")
        r.close()
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(messagetosend))
        self.end_headers()
        self.wfile.write(messagetosend)
        return

server_address_httpd = ('192.168.100.10', 80)
httpd = HTTPServer (server_address_httpd, RequestHandler_httpd)
print('Starting Server...')
httpd.serve_forever()
print(req)