#!/usr/bin/env python3
import http.server as SimpleHTTPServer
import socketserver as SocketServer
import cgi
import logging
import argparse
from urllib import parse

parser = argparse.ArgumentParser()
parser.add_argument('-p','--port', default=80, type=int)
parser.add_argument('response', default=200, type=int, nargs='?')
args = parser.parse_args()

class GetHandler(
    SimpleHTTPServer.SimpleHTTPRequestHandler
):

    def do_GET(self):
        logging.error('=GET============================================================')
        logging.error(self.headers)
        self.send_error(args.response)
        logging.error('=END============================================================\n')

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = parse.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            length = int(self.headers['content-length'])
            postvars = self.rfile.read(length)
        logging.error('=POST===========================================================')
        logging.error(self.headers)
        logging.error(postvars)
        self.send_error(args.response)
        logging.error('=END============================================================\n')


Handler = GetHandler
httpd = SocketServer.TCPServer(("", args.port), Handler)

httpd.serve_forever()