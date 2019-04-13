from flask import Flask
import subprocess
from flask import jsonify
#from squid_py.ddo.metadata import Metadata
#from squid_py.ocean import Ocean
#from squid_py.config import Config
from smbus import SMBus
# Import basic packages
import io
import logging
import os
import glob
import warnings

warnings.filterwarnings('ignore')

from time import gmtime, strftime


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Path storing Pi camera photos
img_path = './images'


# Classification using Google Vision API
def proccess_picture():
    all_results = list()
    for img in os.listdir(img_path):
        if img.endswith('.jpg'):
            image = os.path.join(img_path, img)
            logging.info(image)

            with io.open(image, 'rb') as image_file:
                content = image_file.read()

                image = types.Image(content=content)

                response = client.label_detection(image=image)
                labels = response.label_annotations
                logging.info(strftime('%Y-%m-%d %H:%M:%S', gmtime()))
                logging.info('Labels:')
                result = []
                for label in labels:
                    logging.info(label)
                    result.append(label.description)
        all_results.append(result)
    return all_results


app = Flask(__name__)
bus = SMBus(1)
#ocean = Ocean(Config(filename='config.ini'))


@app.route("/api/status", methods=['GET'])
def status():
    return "status"


@app.route("/api/snap", methods=['GET'])
def snap():
    #subprocess.call('flask_app/scripts/take_photos.sh')
    #subprocess.call('/home/pi/git/pines-and-electronics/flask_app/scripts/take_photos.sh')
    this_cmd = "raspistill -t 10000 -tl 2000 -o /home/pi/git/pines-and-electronics/flask_app/images/image%04d.jpg"
    #this_cmd = "raspistill -o cam.jpg"
    #this_cmd = "ls"
    subprocess.call(this_cmd, shell=True)
    print("Ran", this_cmd)
    return 'snap!' + this_cmd


@app.route("/api/register", methods=['GET'])
def register():
    label_list = proccess_picture()

    summary = list()
    for i, label in enumerate(label_list):
        print(i, label)
        summary.append("|".join(label))
    #metadata =Metadata.get_example()
    #metadata['base']['tags'] = labels
    #ddo = ocean.assets.create(metadata, ocean.accounts._accounts[0])
    #return ddo.did
    return " *** ".join(summary)


@app.route("/api/snapshot", methods=['GET'])
def snapshot():
    return "snapshot"


@app.route("/api/linear", methods=['POST'])
def linear():
    bus.write_byte(8, ord("S"))
    return "linear"

@app.route("/api/start", methods=['GET'])
def start():
    bus.write_byte(8, ord("S"))
    return "START"

@app.route("/api/stop", methods=['GET'])
def stop():
    bus.write_byte(8, ord("s"))
    return "STOP"

@app.route("/api/steer", methods=['POST'])
def steer():
    bus.write_byte(9, ord('x'))
    return "steer"


# def publish_asset():
#     return ocean.assets.create(Metadata.get_example())


if __name__ == "__main__":
    app.run(port=3333)
