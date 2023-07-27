from flask import Flask, request, render_template

app = (__name__)

@app.route("/")
def index():
    return "Hello"

@app.route("/")