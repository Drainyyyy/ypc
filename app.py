from flask import Flask, redirect, render_template, request

import config

app = Flask(__name__)
logged_in = False


@app.route('/')
def index():
    print(request.base_url)
    if logged_in:
        return redirect('/chat')
    else:
        return redirect('/login')


@app.route('/login')
def sign():
    return render_template("login.html", base_url=request.base_url)


@app.route('/auth')
def auth():
    return


if __name__ == '__main__':
    app.run(**config.FLASK_RUN_CONFIG)

# pep8
