# KrateLabs

Krate Labs **designs and fabricates** illuminated laser etched displays. The innovative design allows only light to pass through the etched artwork, creating a unique and contemporary design. The contrasting colours from the background, the etching and the high grade plexiglass allow the map to stand out as a very distinct art piece for your home or business.

The lasering process allows us to etch the most intricate details with extreme precision, creating a very unique and detailed image of any location in the entire world.

Our contemporary designs highlights the cartography as the focal point as we fuse and blend the natural and urban landscapes into a design that we highlight with light itself. This allows the piece to stand out and light a room with a natural glow that can create an ambience or compliment an existing decor.

Whether you wish to preserve cityscapes or familiar places, Krate Labs is here to provide meaningful art purchases by allowing each user to choose a location that is meaningful to them. Simply choose from a variety of templates that we currently have, or send a custom request, we’re here to help you create your customized art piece for your home or business.

## How to build SVG

### Build Full Features

**Python (Ubuntu)**

Install

```bash
$ sudo apt-get update && apt-get install potrace -y
$ git clone git@github.com:KrateLabs/KrateLabs.git
$ cd KrateLabs
$ pip install -r requirements.txt
```

```bash
$ mkdir data
$ python ./scripts/svg.py \
  --lng -79.380 \
  --lat 43.652 \
  --zoom 10 \
  --style mapbox://styles/addxy/cilvpgjqs001k9om1ay3jmb75 \
  --filename Full
```

**Docker**

Install

```bash
$ git clone git@github.com:KrateLabs/KrateLabs.git
$ cd KrateLabs
$ docker build kratelabs .
```

Running on Docker allows you to create map SVG from any Operating System without any issues.

```bash
docker run -it --rm -v $HOME/data:/data kratelabs \
  python svg.py \
  --lng -79.380 \
  --lat 43.652 \
  --zoom 10 \
  --style mapbox://styles/addxy/cilvpgjqs001k9om1ay3jmb75 \
  --filename Full
```
### Mapbox Styles

**All Features**

- mapbox://styles/addxy/cilvpgjqs001k9om1ay3jmb75

**Roads Only**

- mapbox://styles/addxy/cilvq1gtm00199llxxre3k6g9

**Water Only**

- mapbox://styles/addxy/cilvpgeq1001j9km8evgj1a1p
