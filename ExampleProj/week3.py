from flask import Flask, request, make_response, url_for, render_template, redirect, abort, session
app = Flask("__name__")
app.secret_key='x£89(+~#nnkl;/m'


app.route('/')
def index():
    if 'username' in session:
        return f'logged in as {session["username"]}'
    else:
        return "Not logged in"
app.route('/login', metthods=["POST", "GET"])
def login():
    if request.method=='POST' and session['username']==request.form.get('username'):
        return redirect(url_for('index'))
    return "<form method=POST> Enter: <input type=text name=username></input><br> <input type=submit name=submit </form>"
app.route('/logout')
def logout():
    session.pop('username', None)
print("hellloo diff ")
    return redirect(url_for('index'))