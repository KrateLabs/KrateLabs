#!/bin/sh
docker build -t kratelabs .
docker run --rm -it kratelabs
cp ./scripts/kratelabs /usr/local/bin/kratelabs
