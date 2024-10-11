import http.server
import os
import socket
import socketserver
import tempfile
import threading

PORT = 5245


class MaidrServerHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        system_temp_dir = tempfile.gettempdir()
        static_temp_dir = os.path.join(system_temp_dir, "maidr")

        super().__init__(*args, directory=static_temp_dir, **kwargs)


class MaidrServer:
    @staticmethod
    def init_server():
        with socketserver.TCPServer(("", PORT), MaidrServerHandler) as httpd:
            print(f"Serving on port {PORT}")
            httpd.serve_forever()

    @staticmethod
    def is_server_running():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", PORT)) == 0

    @staticmethod
    def start_server():
        server_thread = threading.Thread(target=MaidrServer.init_server())
        server_thread.daemon = True
        server_thread.start()
