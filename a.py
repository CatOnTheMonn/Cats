from flask import Flask, session, render_template
import random

def root():
    session['count'] = 0
    return'Hello world <br> <a href="/clicerOwO">≧◠ᴥ◠≦</a>'

app = Flask(__name__)

app.add_url_rule('/', 'root', root)
app.config['SECRET_KEY'] = '123456789'

app.run()