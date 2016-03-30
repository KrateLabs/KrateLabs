FROM python:alpine
MAINTAINER Denis Carriere - carriere.denis@gmail.com

# Install Potrace
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories
RUN apk add --update potrace imagemagick && rm -rf /var/cache/apk/*

# Install Python Requirements
ADD requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

# Install App
ADD setup.py /code/setup.py
ADD kratelabs /code/kratelabs
RUN pip install .

WORKDIR /data
CMD kratelabs --help
