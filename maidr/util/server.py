import os
import socket
import time
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread
from typing import Any

import requests
from htmltools import Tag


def server_handler(path, port):
    class MaidrServerHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            return SimpleHTTPRequestHandler.do_GET(self)

        def __init__(self, *args: Any, **kwargs: Any):
            super().__init__(*args, directory=path, **kwargs)

        def log_message(
            self, format, *args
        ):  # pyright: ignore[reportMissingParameterType]
            pass

    with TCPServer(("", port), MaidrServerHandler) as httpd:
        httpd.serve_forever()


class MaidrServer:
    @staticmethod
    def get_local_ip():
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def run_server(html: Tag):
        ip_address = MaidrServer.get_local_ip()
        file_name = str(int(time.time() * 1000)) + ".html"
        html.save_html(file_name)

        if not MaidrServer.check_server():
            th: Thread = Thread(
                target=server_handler,
                args=(file_name, 6942),
                daemon=True,
            )
            th.start()

        url = "http://" + ip_address + ":6942" + "/" + file_name
        webbrowser.open(url)

    @staticmethod
    def check_server(timeout=2):
        try:
            response = requests.head(
                "http://" + MaidrServer.get_local_ip() + ":6942", timeout=timeout
            )
            return response.status_code == 200
        except requests.ConnectionError:
            return False
