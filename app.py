#!/usr/bin/env python
# Copyright (c) 2018 Usharerose. All rights reserved.
# -*- coding: utf-8 -*-
from flask import Flask, make_response, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
