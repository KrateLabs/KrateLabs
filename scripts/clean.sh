#!/bin/sh
CONTAINERS=$(sudo docker ps -a -q)
IMAGES=$(sudo docker images -q)

# Remove all Docker Containers
if [ -n "$CONTAINERS" ]; then
  docker rm $CONTAINERS
fi

# Remove all Docker Images
if [ -n "$IMAGES" ]; then
  docker rmi $IMAGES
fi

# Remove PNG & SVG Images created
rm -f $(pwd)**/*.png
rm -f $(pwd)**/*.svg

# Remove Python Build
rm -f kratelabs.egg-info/
