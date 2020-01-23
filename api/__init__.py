import os
from flask import Flask, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "storage", "upload")
RESULTS_DIR = os.path.join(BASE_DIR, "storage", "results")
OUTPUT_DIR = os.path.join(BASE_DIR, "storage", "output")

for d in [UPLOAD_DIR, RESULTS_DIR, OUTPUT_DIR]:
    os.makedirs(d, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

@app.route("/")
def home_view():
    return "<h1>Hello world</h1>"

@app.route("/static/uploads/<filename>")
def static_uploads_view(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)