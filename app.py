#!/usr/bin/env python
# Copyright (c) 2018 Usharerose. All rights reserved.
# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
