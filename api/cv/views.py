import os
from flask import request, send_from_directory, url_for
from api import app
from api.utils import handle_file_upload
from .utils import extract

@app.route("/static/outputs/<path:path>")
def static_outputs_view(path):
    # path => Users/cfe/Dev/opencv-rest-api/api/storage/output/15/main.jpg
    dirname = os.path.dirname(path)
    if not dirname.startswith("/"):
        dirname = f"/{dirname}"
    filename = os.path.basename(path)
    print(dirname, filename)
    return send_from_directory(dirname, filename)

@app.route("/api/upload/opencv", methods=['POST'])
def api_upload_opencv():
    if request.method == "POST":
        upload = request.files.get("file")
        dest_dir = app.config['UPLOAD_FOLDER']
        dest_len = len(os.listdir(dest_dir))
        response, status = handle_file_upload(upload, dest_dir, dest_len=dest_len, return_img_path=True)
        if len(f"{status}") == 4:
            extracted_path = extract(response)
            mainjpg = os.path.join(extracted_path, "main.jpg")
            if mainjpg.startswith("/"):
                mainjpg = mainjpg[1:] # mainjpg[0]
            final_url = url_for('static_outputs_view', path=mainjpg, _external=True)
            return {"path": final_url}, 201
        return response, status
    return {"detail": "Not allowed"}, 400