# main.py
import os
from flask import Flask, request, jsonify, send_file
from app.converter import convert_dicom_to_jpg
import tempfile

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    if 'dicom_file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    dicom_file = request.files['dicom_file']
    if dicom_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as tmp_dicom:
        dicom_file.save(tmp_dicom.name)
        jpg_path = tmp_dicom.name + '.jpg'
        convert_dicom_to_jpg(tmp_dicom.name, jpg_path)

        # Send the JPEG file as a response
        return send_file(jpg_path, mimetype='image/jpeg', as_attachment=True, attachment_filename='converted.jpg')

    # Clean up temporary files
    os.remove(tmp_dicom.name)
    os.remove(jpg_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
