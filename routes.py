from flask import Flask, render_template, request, g, jsonify, make_response
# from models import db, User, Product
# from forms import SignupForm, AddProductForm
import os

# NippyWiki - a simple python based wiki using markdown

app = Flask(__name__)
app.secret_key = "development-key"

@app.route("/")
def index():
    """ default page """
    # print("Rendering.index.html")
    return render_template("index.html")
