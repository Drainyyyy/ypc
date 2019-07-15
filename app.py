# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from flask import Flask, redirect, request
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.utils import escape

import config
from ypc.api.errors import account_exceptions
from ypc.models import account
from ypc.models.account import Account
from ypc.models.enums import AccountType, AccountStatus
from ypc.utilities.auth import Auth

app = Flask(__name__)
test_acc = Account("Drainyyy", "xyz12345", 0, AccountType.admin, AccountStatus.accepted)
logged_in = Auth(test_acc)


@app.route("/")
def index():
    raise account_exceptions.AccountException(test_acc)


@app.route("/login", methods=["POST", "GET"])
def sign():
    return None


@app.route('/auth', methods=["POST", "GET"])
def auth():
    try:
        username = escape(request.form["username"])  # TODO security
        password = request.form["password"]
        authentication = Auth(account.Account(username, password, 0, AccountType.admin, AccountStatus.accepted)).login()
        if authentication:
            return redirect("/chat")
        else:
            return redirect("/login")
    except BadRequestKeyError:
        return redirect("/login")


if __name__ == '__main__':
    app.run(**config.FLASK_RUN_CONFIG)
