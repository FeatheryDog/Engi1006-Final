# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def test():
    return render_template("home.html")

@app.route("/pumpkin")
def pumpkin():
    return render_template("pumpkin.html")

@app.route("/internet")
def columbia():
    return render_template("internet.html")

#start the server
if __name__ == "__main__":
    app.run()