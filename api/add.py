from http.server import BaseHTTPRequestHandler
import urllib.parse
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the two numbers from the query parameters
        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        num1 = int(query_components.get('num1', [0])[0])
        num2 = int(query_components.get('num2', [0])[0])

        # Add the two numbers together
        result = num1 + num2

        # Return the result as a JSON object
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps({'result': result})
        self.wfile.write(response.encode())
        return
