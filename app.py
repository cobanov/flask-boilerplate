from flask import Flask, render_template, url_for, redirect, request, flash
import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'


@app.route("/main", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():
    """ some codes """
    return render_template("index.html")


app.run(debug=True)
