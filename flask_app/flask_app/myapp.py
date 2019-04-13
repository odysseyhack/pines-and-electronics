from flask_app.camera.gcp_vision_multi_img import proccess_picture
from flask import Flask
import subprocess
from squid_py.ddo.metadata import Metadata
from squid_py.ocean import Ocean
from squid_py.config import Config
from smbus import SMBus


app = Flask(__name__)
bus = SMBus(1)
ocean = Ocean(Config(filename='config.ini'))


@app.route("/api/status", methods=['GET'])
def status():
    return "status"


@app.route("/api/snap", methods=['GET'])
def snap():
    subprocess.call('flask_app/scripts/take_photos.sh')
    return 'snap'


# @app.route("/api/register", methods=['POST'])
@app.route("/api/register", methods=['GET'])
def register():
    labels = proccess_picture()
    metadata =Metadata.get_example()
    metadata['base']['tags'] = labels
    ddo = ocean.assets.create(metadata, ocean.accounts._accounts[0])
    return ddo.did


@app.route("/api/snapshot", methods=['GET'])
def snapshot():
    return "snapshot"


@app.route("/api/linear", methods=['POST'])
def linear():
    bus.write_byte(8, ord(20))
    return "linear"


@app.route("/api/steer", methods=['POST'])
def steer():
    bus.write_byte(9, ord(20))
    return "steer"


# def publish_asset():
#     return ocean.assets.create(Metadata.get_example())


if __name__ == "__main__":
    app.run(port=3333)
