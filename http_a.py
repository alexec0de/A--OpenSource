
"""
A# - http libs

"""

import http.server
import socketserver

PORT = 9999

Handler = http.server.SimpleHTTPRequestHandler




def check_func_http(func, args = None):
	if func == 'run':
		with socketserver.TCPServer(("", int(args)), Handler)as httpd:
		    print("serving at port", args)
		    httpd.serve_forever()