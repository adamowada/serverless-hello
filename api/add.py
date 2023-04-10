from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from socketserver import ThreadingMixIn
import json
import ssl
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the two numbers from the query parameters
        query_components = parse_qs(urlparse(self.path).query)
        num1 = int(query_components.get('num1', [0])[0])
        num2 = int(query_components.get('num2', [0])[0])

        # Add the two numbers together
        result = num1 + num2

        # GET request to /api/hello
        response = requests.get("https://serverless-hello.vercel.app/api/hello")

        # Return the result as a JSON object
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps({'result': result, 'message': response.text})
        self.wfile.write(response.encode())
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == '__main__':
    server_address = ('', 8443)
    httpd = ThreadedHTTPServer(server_address, handler)

    # Set up SSL
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

    print('Starting HTTPS server at https://localhost:8443')
    httpd.serve_forever()
