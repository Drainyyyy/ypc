# -*- coding: utf-8 -*-

#  Copyright (c) 2019. Drainyyy
#  This project is covered by MIT License
#  https://opensource.org/licenses/MIT

from flask import Flask, redirect, request
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.utils import escape

from ypc.utilities.color import Rgb
from ypc import config
from ypc.models import client
from ypc.models.client import Client
from ypc.models.enums import ClientStatus, ClientState, ClientType
from ypc.auth import Auth

app = Flask(__name__)
test_client = Client("Drainyyy", "xyz12345", 0, ClientType.admin, ClientState.accepted, ClientStatus.fine)
logged_in = Auth(test_client)


@app.route("/")
def index():
    print(str(Rgb(255, 255, 255)))
    return "abc"


@app.route("/login", methods=["POST", "GET"])
def sign():
    return None


@app.route("/auth", methods=["POST", "GET"])
def auth():
    try:
        username = escape(request.form["username"])  # TODO security
        password = request.form["password"]
        authentication = Auth(client.Client(username, password, 0, ClientType.admin, ClientState.accepted, ClientStatus.fine)).login()
        if authentication:
            return redirect("/chat")
        else:
            return redirect("/login")
    except BadRequestKeyError:
        return redirect("/login")


if __name__ == "__main__":
    app.run(**config.FLASK_RUN_CONFIG)
