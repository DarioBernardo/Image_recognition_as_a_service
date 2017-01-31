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




