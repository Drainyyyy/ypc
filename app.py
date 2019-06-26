# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from flask import Flask, redirect, render_template, request
from werkzeug.exceptions import BadRequestKeyError

import config
from models.account import DefaultAccount, RejectedAccount, _BaseAccount
from utilities.auth import Auth

app = Flask(__name__)
logged_in = False


@app.route("/")
def index():
    print(request.base_url)
    if logged_in:
        return redirect("/chat")
    else:
        return redirect("/login")


@app.route("/login", methods=["POST", "GET"])
def sign():
    return render_template("login.html", base_url=request.url_root)# TODO remove and use JS


@app.route('/auth', methods=["POST", "GET"])
def auth():
    try:
        username = request.form["username"]
        password = request.form["password"]
        authentication = Auth(DefaultAccount(username, password, 0)).login()
        if authentication:
            return redirect("/chat")
        else:
            return redirect("/login")
    except BadRequestKeyError:
        return redirect("/login")


if __name__ == '__main__':
    app.run(**config.FLASK_RUN_CONFIG)

# pep8
