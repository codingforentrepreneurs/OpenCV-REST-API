from flask import send_from_directory, request
from api import app, allowed_file

@app.route("/")
def home_view():
    return "<h1>Hello world</h1>"

@app.route("/static/uploads/<filename>")
def static_uploads_view(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/api/upload", methods=["POST"])
def api_upload_view():
    if request.method == "POST":
        print(request.files)
    return "Hello world"