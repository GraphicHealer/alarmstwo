import http.server
import socketserver
import threading

def web():
    PORT = 80
    DIRECTORY = "plugins/Web/public/"


    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)


    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

w = threading.Thread(target=web)

def startup(plug):
    print('Web Starting')
    w.start()