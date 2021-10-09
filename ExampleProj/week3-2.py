from flask import Flask, request, make_response, url_for, render_template, redirect, abort, session
app = Flask("--name--" )
app.secret_key="Hello"
@app.route('/')
def index():
    if 'username' in session:
        return f'logged in as {session["username"]}'
    else:
        return render_template('adduser.html')
@app.route('/login', methods=["POST", "GET"])
def login():
    print(" login called ................................")
    if (session.get('username')==request.form.get('username', 'a')):
        return redirect(url_for('index'))
    else:
       return redirect(url_for('add'))
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index')) 
@app.route('/add', methods=["POST"])
def add():
    print("=============================================", request)
    session['username']=request.form.get('username')
    print("Session ............................................", session['username'], request.form.get ('username', 'h') )
    return "aadde"
