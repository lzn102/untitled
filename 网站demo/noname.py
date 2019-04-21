from flask import Flask, make_response
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/<path>')
def today(path):
    base_dir = os.path.dirname(__file__)
    resp = make_response(open(os.path.join(base_dir, path)).read())
    resp.headers["Content-type"]="application/json;charset=UTF-8"
    return resp


if __name__ == '__main__':
    app.run(debug=True)
