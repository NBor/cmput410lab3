#!/usr/bin/env python
"""Simple HTTP server with CGI."""
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8888)
handler.cgi_directories = ["/cgi"]

httpd = server(server_address, handler)
print 'Starting Server...'
httpd.serve_forever()
