#!/usr/bin/env python3
from flask import Flask
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
    return result
@app.route('/healthz', methods=['GET'])
def healthz():
    return "OK"

# Set port to listen on from arguments
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=sys.argv[1])