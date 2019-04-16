""" routes.py - website rounting environe for NippyWiki """
import os
from flask import Flask, render_template, request, g, jsonify, make_response
from flask_bootstrap import Bootstrap
# from models import db, User, Product
# from forms import SignupForm, AddProductForm


# NippyWiki - a simple python based wiki using markdown

APP = Flask(__name__)
APP.secret_key = "development-key"

def shutdown_server():
    """ shutsdown the SMARSLab web server """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@APP.route('/shutdown')
def shutdown():
    """ requests the web server shutsdown """
    shutdown_server()
    return 'NippyWiki shutting down... Done.'


@APP.route("/")
def index():
    """ default page """
    # print("Rendering.index.html")
    return render_template("index.html")

if __name__ == "__main__":
    Bootstrap(APP)
    APP.run(debug=True)
