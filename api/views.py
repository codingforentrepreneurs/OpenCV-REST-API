import os
from flask import send_from_directory, request
from api import app
from .utils import handle_file_upload

@app.route("/")
def home_view():
    return "<h1>Hello world</h1>"

@app.route("/static/uploads/<filename>")
def static_uploads_view(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/api/upload", methods=["POST"])
def api_upload_view():
    if request.method == "POST":
        upload = request.files.get("file")
        dest_dir = app.config['UPLOAD_FOLDER']
        dest_len = len(os.listdir(dest_dir))
        return handle_file_upload(upload, dest_dir, dest_len=dest_len)
    return {"detail": "Not allowed"}, 400