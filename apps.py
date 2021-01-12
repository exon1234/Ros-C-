from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('http://www.sjzd.site/static/1.jpg')
