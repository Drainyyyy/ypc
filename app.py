from flask import Flask, redirect, render_template, request
from werkzeug.exceptions import BadRequestKeyError

import config
from models.account import Account
from utilities.auth import Auth

app = Flask(__name__)
logged_in = False

# TODO Copyright!
@app.route('/')
def index():
    print(request.base_url)
    if logged_in:
        return redirect('/chat')
    else:
        return redirect('/login')


@app.route('/login', methods=["POST", "GET"])
def sign():
    print(request.url_root)
    return render_template("login.html", base_url=request.url_root)


@app.route('/auth', methods=["POST", "GET"])
def auth():
    try:
        _username = request.form["username"]
        _password = request.form["password"]
        _auth = Auth(Account(_username, _password)).login()
        if _auth:
            return redirect("/chat")
        else:
            return redirect("/login")
    except BadRequestKeyError:
        return redirect("/login")


if __name__ == '__main__':
    app.run(**config.FLASK_RUN_CONFIG)

# pep8
