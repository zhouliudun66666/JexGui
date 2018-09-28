#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  @author: WuBingBing


from flask import Flask, render_template,request
# from urllib import request
import urllib
import os

app = Flask(__name__)
imagepath = os.path.join(os.getcwd(),"static/images")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    os.system("python starttest.py")
    return render_template('index.html')

# @app.route('/start', methods=['GET'])
# def start():
#     return render_template('indexload.html')

@app.route('/report', methods=['GET'])
def report():
    return render_template('report.html')

@app.route('/new_add',methods=['GET'])
def login_index():
    return render_template('new_add.html')

@app.route('/add',methods=['POST'])
def add():
    username = request.form.get('username','default value')
    password = request.form.get('password','default value')
    print(username)
    print(password)
    return render_template('new_add.html')

@app.route('/list', methods=['GET'])
def get_list():
    return render_template('list.html')

if __name__ == '__main__':
    app.run(host='192.168.0.165',port=5000,debug=True)