#!/bin/sh
CONTAINERS=$(sudo docker ps -a -q)
IMAGES=$(sudo docker images -q)

# Remove all Docker Containers
if [ -n "$CONTAINERS" ]; then
  sudo docker rm $CONTAINERS
fi

# Remove all Docker Images
if [ -n "$IMAGES" ]; then
  sudo docker rmi $IMAGES
fi

# Remove PNG & SVG Images created
sudo rm -f $(pwd)**/*.png
sudo rm -f $(pwd)**/*.svg

# Remove Python Build
rm -f kratelabs.egg-info/
