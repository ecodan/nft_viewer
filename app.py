from flask import Flask
from flask import render_template, request
from jinja2 import TemplateNotFound
from flask_restful import Resource, Api

app = Flask(__name__)



@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('index.html'), 404


class TokenList(Resource):
    def get(self, address):
        return TODOS


if __name__ == '__main__':
    app.run()
