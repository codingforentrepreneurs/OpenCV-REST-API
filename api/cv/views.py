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


def get_url_for_local_image(dirname, filename):
    if dirname.startswith("/"):
        dirname = dirname[1:]
    final_path = os.path.join(dirname, filename)
    return url_for('static_outputs_view', path=final_path, _external=True)

@app.route("/api/upload/opencv", methods=['POST'])
def api_upload_opencv():
    if request.method == "POST":
        upload = request.files.get("file")
        dest_dir = app.config['UPLOAD_FOLDER']
        dest_len = len(os.listdir(dest_dir))
        response, status = handle_file_upload(upload, dest_dir, dest_len=dest_len, return_img_path=True)
        if len(f"{status}") == 4:
            extracted_path = extract(response)
            final_url = get_url_for_local_image(extracted_path, "main.jpg")
            # final_items = [get_url_for_local_image(extracted_path, x) for x in os.listdir(extracted_path) if x.endswith('.jpg')]
            response = {"path": final_url}
            faces_dir = os.path.join(extracted_path, 'faces')
            faces_items = [get_url_for_local_image(faces_dir, x) for x in os.listdir(faces_dir) if x.endswith('.jpg')]
            faces_count = len(faces_items)
            response['faces_count'] = faces_count
            response['faces'] = faces_items
            return response, 201
        return response, status
    return {"detail": "Not allowed"}, 400