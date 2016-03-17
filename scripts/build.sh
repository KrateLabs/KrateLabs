#!/bin/bash

# Build Roads
python kratelabs.py \
  --lng -79.380 \
  --lat 43.652 \
  --zoom 10 \
  --style mapbox://styles/addxy/cilvq1gtm00199llxxre3k6g9 \
  --filename Roads \
  --upload

# Build Water
python kratelabs.py \
  --lng -79.380 \
  --lat 43.652 \
  --zoom 10 \
  --style mapbox://styles/addxy/cilvpgeq1001j9km8evgj1a1p \
  --filename Water \
  --upload

# Build All
python kratelabs.py \
  --lng -79.380 \
  --lat 43.652 \
  --zoom 10 \
  --style mapbox://styles/addxy/cilvpgjqs001k9om1ay3jmb75 \
  --filename Full \
  --upload
