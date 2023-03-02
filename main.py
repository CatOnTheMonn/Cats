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
        cat_breed = request.form.get('cat')
        if cat_breed in cats:
            return render_template('cat_info.html', breed=cat_breed, cat_info=cats[cat_breed]['info'], image=cats[cat_breed]['image'])
        else:
            return render_template('not_found3.0.html')

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)

app.add_url_rule('/', 'root', root)
app.add_url_rule('/cat', 'cat', cat, methods=['POST', 'GET'])
app.config['SECRET_KEY'] = '123456789'

app.run()