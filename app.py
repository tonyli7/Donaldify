# imports

from flask import Flask, render_template, request, session, redirect, url_for,Markup
import sqlite3, utils

#flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    if 'un' in session and session['un'] != 0:
        return render_template("home.html",un=session['un'])
    else:
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
        #button = request.form['button']
        user = request.form['in_username']
        passwd = request.form['in_password']

        if utils.loginauth(user,passwd):
            session['un'] = user
            session['pw'] = passwd
            return redirect(url_for("blog"))
        else:
            error = "INVALID USERNAME AND/OR PASSWORD"
            return render_template("login.html",error=error)

@app.route("/logout")
def logout():
    session['un'] = 0
    session['pw'] = 0
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/blog", methods=["GET", "POST"])
def blog():
    if 'un' not in session or session['un']==0:
        return redirect(url_for("home"))
    else:
        user = session['un']
        s = ""
        stories = utils.getAllPosts()
        for p in stories:
            s += "<h1> <a href='story/%s'> %s</a> </h1>" %(p[1], p[1])
            s += "<h2> Posted by: %s </h2>" %p[0]
            s += "<h3> %s </h3>" %p[2] + "<hr>"
        s = Markup(s)
        return render_template("blog.html",un=user,stories=s)
        
if __name__ == "__main__":
    app.debug = True
    app.secret_key = "whatsthisfor"
    app.run(host='0.0.0.0',port=8000)
