# Base Image
FROM python:3.10.2-slim

COPY . /app
WORKDIR /app

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
        gcc \
        make \
        locales \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Update Locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Create a virtual environment in /opt
RUN python3 -m venv /opt/venv

# Install requirments to new virtual environment
RUN /opt/venv/bin/pip install -r requirements.txt

# purge unused
RUN apt-get remove -y --purge git make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

CMD /opt/venv/bin/gunicorn api.wsgi:app --bind "0.0.0.0:${PORT:-8000}"
