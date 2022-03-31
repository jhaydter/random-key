#!/usr/bin/env python3
from webbrowser import get
from flask import Flask, redirect, url_for
from base64 import b64encode
from waitress import serve
import os
import sys
import logging

# set logging level
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Flask(__name__)

# Flask route which uses path to generate variable number of bytes and returns result in base64
@app.route('/key/<int:bytes_number>', methods=['GET'])
def get_hash(bytes_number):
    result = b64encode(os.urandom(bytes_number))
    return result + b'\n'

# define healthcheck path used by k8s deployment
@app.route('/healthz', methods=['GET'])
def healthz():
    return "OK"

# route for any path not found to redirect to get_hash function
@app.errorhandler(404)
def page_not_found(error):
#    return redirect(url_for('get_hash', bytes_number=404))
    return "HTTP 404: Try path /key/$integer \n", 404

# Set port to listen on from arguments
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=sys.argv[1])