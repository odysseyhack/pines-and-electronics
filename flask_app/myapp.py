from flask import Flask
from squid_py.ocean import ocean
app = Flask(__name__)


@app.route("/", methods=['POST'])
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(port=3333)