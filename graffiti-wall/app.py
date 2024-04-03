#!/usr/bin/env python

from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
from datetime import datetime

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": "porkandrice"  # username: password
}

@auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]:
        return username

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def index():
    if request.method == 'POST':
        text = request.form['text']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = f'{timestamp} - {text}'
        with open('graffiti_wall.txt', 'a') as file:
            file.write(entry + '\n')
            file.write('=' * 40 + '\n')
    return render_template('index.html')

@app.route('/graffiti_wall')
@auth.login_required
def graffiti_wall():
    with open('graffiti_wall.txt', 'r') as file:
        graffiti = file.read()
    return render_template('graffiti_wall.html', graffiti=graffiti)

if __name__ == '__main__':
    app.run()