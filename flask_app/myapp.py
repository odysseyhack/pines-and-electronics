from flask import Flask
from squid_py.ddo.metadata import Metadata
from squid_py.ocean import Ocean

app = Flask(__name__)

# ocean = Ocean()


@app.route("/api/status", methods=['GET'])
def status():
    return "status"


@app.route("/api/snap", methods=['GET'])
def snap():
    return "snap"


@app.route("/api/register", methods=['POST'])
def register():
    return "register"


@app.route("/api/snapshot", methods=['GET'])
def snapshot():
    return "snapshot"


@app.route("/api/linear", methods=['POST'])
def linear():
    return "linear"


@app.route("/api/steer", methods=['POST'])
def steer():
    return "steer"


# def publish_asset():
#     return ocean.assets.create(Metadata.get_example())


if __name__ == "__main__":
    app.run(port=3333)
