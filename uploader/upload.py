import os
import requests

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# filepath = os.path.join(BASE_DIR, 'abc.png')
# files = {"file": open(filepath, 'rb')}
# url = 'http://127.0.0.1:8000/api/upload'
# r = requests.post(url, files=files)
# print(r.text)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, 'has_faces.jpg')
files = {"file": open(filepath, 'rb')}
# url = 'http://127.0.0.1:8000/api/upload/opencv'
# url = 'http://0.0.0.0:8000/api/upload/opencv'
url = 'https://opencv-rest-api-app.herokuapp.com/api/upload/opencv'
r = requests.post(url, files=files)
print(r.text)