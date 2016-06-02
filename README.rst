KrateLabs
=========

Krate Labs **designs and fabricates** illuminated laser etched displays.
The innovative design allows only light to pass through the etched
artwork, creating a unique and contemporary design. The contrasting
colours from the background, the etching and the high grade plexiglass
allow the map to stand out as a very distinct art piece for your home or
business.

The lasering process allows us to etch the most intricate details with
extreme precision, creating a very unique and detailed image of any
location in the entire world.

Our contemporary designs highlights the cartography as the focal point
as we fuse and blend the natural and urban landscapes into a design that
we highlight with light itself. This allows the piece to stand out and
light a room with a natural glow that can create an ambience or
compliment an existing decor.

Whether you wish to preserve cityscapes or familiar places, Krate Labs
is here to provide meaningful art purchases by allowing each user to
choose a location that is meaningful to them. Simply choose from a
variety of templates that we currently have, or send a custom request,
we’re here to help you create your customized art piece for your home or
business.

Install
-------

**Simple Setup**

.. code:: bash

    $ git clone git@github.com:KrateLabs/KrateLabs.git
    $ cd KrateLabs
    $ make
    $ kratelabs --location "CN Tower, Toronto" --zoom 12

    [OK] Geocoded: CN Tower, Toronto, ON M5V, Canada [43.6425657, -79.38705569999999]
    [OK] Created: CN Tower, Toronto.png
    [OK] Created: CN Tower, Toronto.svg

**Using Docker**

.. code:: bash

    $ docker build -t kratelabs .
    $ docker run -it --rm -v $(pwd):/data kratelabs --location "CN Tower, Toronto" --zoom 12

Command Line Interface
----------------------

.. code:: bash

    $ kratelabs --help

::

    Usage: kratelabs [OPTIONS]

      Command Line Interface.

    Options:
    --filename TEXT         Filename output to SVG
    --lat FLOAT             latitude for the center point of the static map;
                            number between  -90 and  90
    --lng FLOAT             longitude for the center point of the static map;
                            number between  -180 and  180
    --location TEXT         Geographical Location based on Google Maps
    --zoom FLOAT            zoom level; number between  0 and  22 . Fractional
                            zoom levels will be rounded to two decimal places.
    --width INTEGER RANGE   width of the image in pixels
    --height INTEGER RANGE  height of the image in pixels
    --style TEXT            mapbox://styles/{username}/{style_id}
    --access_token TEXT     Mapbox access token
    --bearing FLOAT         Rotates the map around its center. Number between 0
                            and 360.
    --pitch FLOAT           Tilts the map, producing a perspective effect.
                            Number between 0 and 60.
    --retina                [boolean] If  @2x is added to request a retina 2x
                            image will be returned
    --attribution           [boolean] Value controlling whether there is
                            attribution on the image; defaults to  false
    --logo                  [boolean] Value controlling whether there is a
                            Mapbox logo on the image; defaults to  false
    --upload                [boolean] Upload to AWS S3
    --delete                [boolean] Delete PNG
    --help                  Show this message and exit.

Mapbox Styles
~~~~~~~~~~~~~

**All Features**

-  mapbox://styles/addxy/cim6u5lfi00k2cwm23exyzjim

**Roads Only**

-  mapbox://styles/addxy/cim6u8zc300om9jm05ku5zurt

**Water Only**

-  mapbox://styles/addxy/cim6u6b7t001l9klzpio0dhaa
