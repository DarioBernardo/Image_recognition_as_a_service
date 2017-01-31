FROM continuumio/anaconda3
MAINTAINER DarioBernardo

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y nano
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY conda_environment.yml /usr/src/app/
RUN conda env create -f conda_environment.yml

COPY . /usr/src/app

RUN chmod u+x run.sh