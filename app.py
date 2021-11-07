from flask import Flask
from flask import render_template, request
from jinja2 import TemplateNotFound

app = Flask(__name__)



@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
