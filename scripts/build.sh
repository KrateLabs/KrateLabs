#!/bin/sh
sudo docker build -t kratelabs .
sudo docker run --rm -it kratelabs
sudo cp ./scripts/kratelabs /usr/local/bin/kratelabs
