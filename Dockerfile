# Base Image
FROM python:3.7

RUN mkdir /app
WORKDIR /app

ADD . /app

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
# Install system dependencies with OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        libopencv-dev \ 
        build-essential \
        libssl-dev \
        libpq-dev \
        libcurl4-gnutls-dev \
        libexpat1-dev \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pip3 install opencv-contrib-python

RUN pipenv install --skip-lock --system --dev

CMD gunicorn api.wsgi:app --bind 0.0.0.0:$PORT
