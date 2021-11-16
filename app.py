from flask import Flask
from flask import render_template, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.after_request
def set_headers(response):
    return response



@app.route('/', methods=['GET'])
def index():
    print("serving index.htlm")
    return render_template('index.html'), 200



if __name__ == '__main__':
    print("running flask app...")
    app.run(host='0.0.0.0', port=5000)
