from flask import Flask
import random
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from CI/CD Sage!"

@app.route('/random')
def maybe_fail():
    if random.random() < 0.5:
        return "Success!"
    else:
        return "Failure!", 500

@app.route('/slow')
def slow_response():
    time.sleep(2)
    return "Slow but OK"
