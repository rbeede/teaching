# © 2023 Rodney Beede

import http.server

static_message = "The developers never expect anyone to reach this port directly. You'd have to have used SSRF (or found a misconfigured firewall) to see this. Any calls made would bypass all authentication and authorization logic. Please cut a finding."

class SimpleReply(http.server.BaseHTTPRequestHandler):
	def _set_response(self, message):
		self.send_response(200)
		self.send_header("Content-Type", "application/json")
		self.end_headers()
		self.wfile.write(bytes(message, "utf-8"))

	def do_HEAD(self):
		self._set_response("")

	def do_GET(self):
		self._set_response(static_message)

	def do_POST(self):
		self._set_response(static_message)


server = http.server.HTTPServer(
    ('', 8080),
    SimpleReply
    )

print("listening...")

server.serve_forever()
