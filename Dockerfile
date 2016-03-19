FROM python:wheezy
MAINTAINER Denis Carriere - carriere.denis@gmail.com

RUN pip install pip --upgrade
RUN apt-get update && apt-get install potrace -y

ADD ./scripts/requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /data
ADD ./scripts .
CMD [ "/bin/bash" ]
