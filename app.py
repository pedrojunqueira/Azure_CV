import base64

from flask import Flask, render_template, request, redirect

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import numpy as np
import cv2
import os

from io import BytesIO
from collections import defaultdict

SUBSCRIPTION_KEY  = os.environ.get("SUBSCRIPTION_KEY", False)
END_POINT = os.environ.get("END_POINT", False)

ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png']

def allowed_extention(filename):
    return True if os.path.splitext(filename)[-1].lower() in ALLOWED_EXTENSIONS else False


def analyse_image(byte_image, buffered_img, END_POINT, SUBSCRIPTION_KEY):

    computervision_client = ComputerVisionClient(END_POINT, CognitiveServicesCredentials(SUBSCRIPTION_KEY))
    
    analysis_type = ["brands"]
    
    image_analysis = computervision_client.analyze_image_in_stream(buffered_img, analysis_type)

    nparr = np.frombuffer(byte_image, np.uint8)
    cv2_image = cv2.imdecode(nparr,flags=1) 

    processed_img = cv2_image.copy()

    brands_detected = len(image_analysis.brands)

    brands = list()

    if brands_detected ==0:
        print("no brands detected")
    else:
        for brand in image_analysis.brands:
            cv2.rectangle(processed_img, (brand.rectangle.x, brand.rectangle.y), 
                        (brand.rectangle.x+brand.rectangle.w, brand.rectangle.y+brand.rectangle.h), (0, 0, 255), 2)
            cv2.putText(processed_img, brand.name, (brand.rectangle.x-5, brand.rectangle.y-5), 
	                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            brands.append(brand.name)

    # Convert captured image to JPG
    _ , buffer = cv2.imencode('.jpg', processed_img)

    # Convert to base64 encoding and show start of data
    processed_img_data = base64.b64encode(buffer)

    encoded_img_data = base64.b64encode(byte_image)

    return encoded_img_data, processed_img_data, brands_detected, brands



# TODO

# 4. capture brand label name and list
# 6. conteiraraze the app
# 7. fix import order
# 8. create function modules
# 9. streach create a class to manage image encode decode state.
# 10. Flash message image extension not allow

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if not allowed_extention(image.filename):
                print("file extention not allowed")
                return redirect(request.url)

            im = image.read()

            buffered_img = BytesIO(im)

            (encoded_img_data, 
            processed_img_data, 
            brands_detected, 
            brands)= analyse_image(im, buffered_img, END_POINT, SUBSCRIPTION_KEY)

    
            return render_template("brand.html", img_data=encoded_img_data.decode('utf-8')
                                    ,img_data2=processed_img_data.decode('utf-8')
                                    ,brands_detected=brands_detected 
                                     , brands=brands)


    return render_template("upload_image.html")
    
if __name__ == "__main__":

    app.run(debug=True, port=5000)