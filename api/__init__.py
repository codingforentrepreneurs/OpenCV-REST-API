import os
from flask import Flask, send_from_directory, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "storage", "upload")
RESULTS_DIR = os.path.join(BASE_DIR, "storage", "results")
OUTPUT_DIR = os.path.join(BASE_DIR, "storage", "output")
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

for d in [UPLOAD_DIR, RESULTS_DIR, OUTPUT_DIR]:
    os.makedirs(d, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR
app.config['OUTPUT_DIR'] = OUTPUT_DIR
app.config['SERVER_NAME'] = '127.0.0.1:8000'

def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


from .views import *
from .cv.views import *