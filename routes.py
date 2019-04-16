""" routes.py - website rounting environe for NippyWiki """
import os
from flask import Flask, render_template, request, g, jsonify, make_response
# from models import db, User, Product
# from forms import SignupForm, AddProductForm


# NippyWiki - a simple python based wiki using markdown

APP = Flask(__name__)
APP.secret_key = "development-key"

@APP.route("/")
def index():
    """ default page """
    # print("Rendering.index.html")
    return render_template("index.html")

if __name__ == "__main__":
    APP.run(debug=True)
