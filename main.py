from flask import Flask, session, render_template, request
import random
import os
from cats_info import cats


def root():
    session['count'] = 0
    # return'Hello world <br> <a href="/clicerOwO">≧◠ᴥ◠≦</a>'
    return render_template('index.html')

def cat():
    if request.method == 'POST':
        if request.form.get('cat') in cats:
            return cats[request.form.get('cat')]

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)

app.add_url_rule('/', 'root', root)
app.add_url_rule('/cat', 'cat', cat, methods=['POST', 'GET'])
app.config['SECRET_KEY'] = '123456789'

app.run()