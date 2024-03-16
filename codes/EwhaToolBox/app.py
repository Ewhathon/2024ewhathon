import io
import sys
import json

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/user")
def user():
    return ""

@app.route("/user/signup", methods=['POST'])
def reg_user():
    user_id = request.args.get('user_id')
    pw = request.args.get('pw')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    address = request.args.get('address')

@app.route("/user/signin")
def login():
    return ""


if __name__ == "main":
    app.run(host = "0.0.0.0")