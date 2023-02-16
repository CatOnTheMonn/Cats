from flask import Flask, session, render_template
import random
import os

def root():
    session['count'] = 0
    # return'Hello world <br> <a href="/clicerOwO">≧◠ᴥ◠≦</a>'
    return render_template('index.html')

folder = os.getcwd()
app = Flask(__name__, template_folder=folder, static_folder=folder)

app.add_url_rule('/', 'root', root)
app.config['SECRET_KEY'] = '123456789'

app.run()