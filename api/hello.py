from http.server import BaseHTTPRequestHandler
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        # GET request to /api/date
        response = requests.get("https://serverless-hello.vercel.app/api/date")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = f'Hello from Python serverless function! The time is: {response.text}'
        self.wfile.write(message.encode())
        return
