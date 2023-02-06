from flask import Flask
import random

def root():
    return'Hello world' + str(random.randint(1, 100))

app = Flask(__name__)

app.add_url_rule('/', 'root', root)

app.run()