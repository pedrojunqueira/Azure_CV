import base64

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"


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