from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "whatsthisfor"
    app.run(host='0.0.0.0',port=8000)
