import os
from flask import request
from api import app
from api.utils import handle_file_upload
from .utils import extract


@app.route("/api/upload/opencv", methods=['POST'])
def api_upload_opencv():
    if request.method == "POST":
        upload = request.files.get("file")
        dest_dir = app.config['UPLOAD_FOLDER']
        dest_len = len(os.listdir(dest_dir))
        response, status = handle_file_upload(upload, dest_dir, dest_len=dest_len, return_img_path=True)
        if len(f"{status}") == 4:
            extracted_path = extract(response)
            return {"path": extracted_path}, 201
        return response, status
    return {"detail": "Not allowed"}, 400