from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 5020

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
print(f"Server running on port {PORT}...")
server.serve_forever()
