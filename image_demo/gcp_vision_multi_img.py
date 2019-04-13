# Import basic packaes
import io
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
img_path = './image_demo/images'

# Classification using Google Vision API
for img in os.listdir(img_path):
	if img.endswith('.jpg'): 
		image = os.path.join(img_path, img)
		print(image)
		
		with io.open(image, 'rb') as image_file:
			content = image_file.read()
			
			image = types.Image(content=content)
			
			response = client.label_detection(image=image)
			labels = response.label_annotations
			print(strftime('%Y-%m-%d %H:%M:%S', gmtime()))
			print('Labels:')
			for label in labels:
				print(label.description)
	
				
	
