#!/usr/bin/env python
# Copyright (c) 2018 Usharerose. All rights reserved.
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import Flask, make_response, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from models import session as db_session
from models import User, Role


DATABASE_URI = 'mysql://appannie:appannie@localhost:3306/blog'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


db = SQLAlchemy(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = db_session.query(User).filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db_session.add(user)
            db_session.commit()
            session['known'] = False
        else:
            session['known'] = True
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    response = make_response(render_template('index.html',
                                             current_time=datetime.utcnow(), form=form, name=session.get('name'),
                                             known=session.get('known', False)))
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    manager.run()
