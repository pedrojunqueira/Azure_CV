# Azure_CV


## Usage

### Create an Azure Computer Vision Instance End point

create a `.evn` file in the main directory

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
