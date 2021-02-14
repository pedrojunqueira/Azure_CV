# Azure_CV

## application architecture

![alt text](https://github.com/pedrojunqueira/Azure_CV/blob/master/Azure_Cognitive_ACI.png?raw=true)


## Usage

### Create an Azure Computer Vision Instance End point

create a `.env` file in the main directory

```.env

SUBSCRIPTION_KEY=<SUBSCRIPTION_KEY>
END_POINT=<END_POINT>

```

More information [here](https://docs.microsoft.com/en-gb/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?tabs=visual-studio&pivots=programming-language-python)


then just...    

```bash

docker-compose up --build

```

app will run on http://0.0.0.0:5000/upload-image

upload image extensions .jpg, jpeg or .png and the app will detect brand

It is using Azure Cognitive Services which is a AI API for various services such as image classification, object detection, speech etc.

## Stop the app just  

`ctrl C` or `docker-compose down`

Here is a screenshot


![alt text](https://github.com/pedrojunqueira/Azure_CV/blob/master/Screen_Shot.png?raw=true)


## Deploy to Azure Container Instance

```bash
# 1 Login to Azure 

docker azure login

# 2 check contexts

docker context ls 

# 3 if context does not exist then create

docker context create aci azurecloud

# 4 change context

docker context use azurecloud

# 5 run container command to deploy to ACI

docker run -d -p 5000:5000 -e SUBSCRIPTION_KEY=<SUBSCRIPTION_KEY> -e END_POINT=<END_POINT> imageregistry/flask-cv_web:latest python app.py 

# 8 Find port and IP where the container is running

docker ps

# 9 go to your browser and access container

```
