#!/bin/python

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/home.html')
def home():
    return render_template('home.html')
@app.route('/menu.html')
def menu():    
    return render_template('menu.html')

@app.route('/aboutUs.html')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/contactUs.html')
def contactUs():
    return render_template('contactUs.html')

app.run(host="0.0.0.0", port=5008)
