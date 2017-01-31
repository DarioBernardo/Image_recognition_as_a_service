# Image recognition as a service

This project uses the Google Tensorflow api to classify any picture on the internet

It uses links as the following:

`http://www.hvac2000.com/wp-content/uploads/2016/05/Orange-Images-6.jpg`

and return a JSON classifying the image, like the following:

`
{
  "orange": 0.9540771842002869, 
  "lemon": 0.0071089621633291245, 
  "banana": 0.002119163516908884, 
  "strawberry": 0.0005894483765587211, 
  "pineapple, ananas": 0.0005539731937460601
}
`

To launch the microservice, just enter the folder and type

`docker-compose up`

Before interacting with the app, wait for the following message:

`python_app_1  | Succesfully downloaded inception-2015-12-05.tgz 88931400 bytes.`

The app needs to download the deep network model from the internet first. It will take a couple of seconds.

To get an image classification, you can use the /classify entrypoing with the "link" attribute to specify an image URL.
Like the example below.

` http://localhost/classify?link=http%3A%2F%2Fwww.hvac2000.com%2Fwp-content%2Fuploads%2F2016%2F05%2FOrange-Images-6.jpg `

Alternatively, you can just go to http://localhost and use the GUI there on that page.

NOTE: The software do not work with HTTPS links! Furthermore it works with 'jpg' images only.


MIT Lincence

