FROM python:3.9.1
RUN apt-get update
ADD . /rottenTomatoRaiting
WORKDIR /rottenTomatoRaiting
RUN pip install -r requirements.txt