# imports

from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

#flask
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "whatsthisfor"
    app.run(host='0.0.0.0',port=8000)
