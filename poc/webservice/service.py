import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.getcwd() + "/poc/webservice/templates", static_folder=os.getcwd() + "/poc/webservice/static")

@app.route("/")
def hello_world():
    return render_template('_base.html')