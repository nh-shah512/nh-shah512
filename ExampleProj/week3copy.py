from flask import Flask, request, make_response, url_for, render_template, redirect, abort, session
from flask import Flask, request, make_response, redirect, url_for, render_template 
app = Flask("--name--")
@app.route('/')
def index():
    if request.cookies.get('user'):
        return request.cookies.get('user')
    else:
        return redirect(url_for('log_in', name='Hello'))

@app.route('/log_in/<name>')
def log_in(name):
    response = make_response(render_template("login.html", name=name))
    response.set_cookie('user','user_name')
    return response