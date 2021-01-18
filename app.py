import os
from pathlib import Path
import json

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import io
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("upload_image.html")


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            im = image.read()

            encoded_img_data = base64.b64encode(im)

            return render_template("brand.html", img_data=encoded_img_data.decode('utf-8'))


    return render_template("upload_image.html")
    
if __name__ == "__main__":

    app.run(debug=True, port=5000)