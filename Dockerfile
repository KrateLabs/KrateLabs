# VERSION:		  0.1
# DESCRIPTION:	  Run kratelabs CLI in a container
# AUTHOR:		  Denis Carriere <carriere.denis@gmail.com>
# COMMENTS:
#	This file describes how to build kratelabs in a container with all
#	dependencies installed.
#	Tested on Ubuntu Willy
# USAGE:
#	# Download kratelabs Dockerfile
#	wget https://raw.githubusercontent.com/KrateLabs/KrateLabs-CLI/master/Dockerfile
#
#	# Build kratelabs image
#	docker build -t kratelabs .
#
#	docker run -it --rm -v $(pwd):/data kratelabs --location "CN Tower, Toronto" --zoom 12
#

# Base docker image
FROM python:alpine
MAINTAINER Denis Carriere <carriere.denis@gmail.com>

# Install Potrace & imagemagick
RUN apk update && apk add \
        potrace imagemagick \
        --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
        && rm -rf /var/cache/apk/*

# Install Python Requirements
ADD requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install pip --upgrade
RUN pip install -r requirements.txt

# Install App
COPY setup.py /src/setup.py
COPY kratelabs /src/kratelabs
RUN pip install .

WORKDIR /data

# Autorun kratelabs
ENTRYPOINT ["kratelabs"]
CMD ["--help"]
