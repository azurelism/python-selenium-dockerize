FROM python:3.8-alpine

LABEL maintainer="azure <azure@cinnamon.is>"

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN mkdir /automation-test
WORKDIR /automation-test

COPY . .
RUN mkdir reports screenshots

RUN pip install -r requirements.txt


