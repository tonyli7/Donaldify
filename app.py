# imports

from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

#flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        if 'un' in session and session['un'] != 0:
            user = session['un']
            return render_template("login.html",un=user)
        else:
            return render_template("login.html",unlogged="You are not currently logged in.")
    else:
        button = request.form['button']
        user = request.form['username']
        passwd = request.form['password']
        if button=="logout":
            session['un'] = 0
            session['pw'] = 0
            return render_template("home.html")
        else:
            if utils.loginauth(user,passwd):
                session['un'] = user
                session['pw'] = passwd
                return redirect(url_for("home"))
            else:
                error = "INVALID USERNAME AND/OR PASSWORD"
                return render_template("login.html",error=error)

@app.route("/register")
def register():
    return render_template("register.html")

# @app.route("/blog")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "whatsthisfor"
    app.run(host='0.0.0.0',port=8000)
