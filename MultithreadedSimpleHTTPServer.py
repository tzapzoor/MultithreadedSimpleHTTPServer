#!/bin/env python

try:
    # Python 2.x
    from SocketServer import ThreadingMixIn
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
except ImportError:
    # Python 3.x
    from socketserver import ThreadingMixIn
    from http.server import SimpleHTTPRequestHandler, HTTPServer

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

import sys
import os

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 80

print '\n>>> Starting HTTP Server on port ' + str(port)

if sys.argv[2:]:
    os.chdir(sys.argv[2])

print '>>> Directory to share: ' + os.getcwd()

server = ThreadingSimpleServer(('', port), SimpleHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print '\nServer has stopped!'
