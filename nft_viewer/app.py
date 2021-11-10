from flask import Flask
from flask import render_template, request
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.route('/')
def index():
    print("serving index.htlm")
    return render_template('index.html'), 404


if __name__ == '__main__':
    print("running flask app...")
    app.run(host='0.0.0.0', port=5000)
