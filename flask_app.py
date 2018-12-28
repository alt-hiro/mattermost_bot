# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:31:48 2018

@author: takano.hiroyuki
"""

# server.py
import json
from flask import Flask, request

app = Flask(__name__)

"""
@app.route('/')
def index():
    return 'Hello'
"""
@app.route('/matter', methods=['POST'])
def post():
    data = request.json
    print(data)
    return json.dumps(dict())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
