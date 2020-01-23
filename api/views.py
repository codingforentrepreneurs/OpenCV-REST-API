import os
from flask import send_from_directory, request
from api import app, allowed_file
from werkzeug.utils import secure_filename

@app.route("/")
def home_view():
    return "<h1>Hello world</h1>"

@app.route("/static/uploads/<filename>")
def static_uploads_view(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/api/upload", methods=["POST"])
def api_upload_view():
    if request.method == "POST":
        print(request.files.get("file"))
        upload = request.files.get("file")
        if upload == None:
            return {"detail": "File not found"}, 404
        if upload.filename == "" and allowed_file(upload.filename):
            return {"detail": "Filename not valid"}, 400
        filename = secure_filename(upload.filename)
        length_dest_dir = len(os.listdir(app.config['UPLOAD_FOLDER']))
        _, ext = os.path.splitext(filename)
        new_filename = f"{length_dest_dir}{ext}"
        dest_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        upload.save(dest_path)
    return "Hello world"