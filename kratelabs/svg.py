#!/usr/bin/python
# coding: utf8

"""Krate Labs.

SVG module
"""

from __future__ import absolute_import
import subprocess
import click
import os
import requests
import geocoder
import sys


@click.command()
@click.option('--filename', help='Filename output to SVG')
@click.option('--lat', type=click.FLOAT, help='latitude for the center point of the static map; number between  -90 and  90')
@click.option('--lng', type=click.FLOAT, help='longitude for the center point of the static map; number between  -180 and  180')
@click.option('--location', help='Geographical Location based on Google Maps')
@click.option('--zoom', type=click.FLOAT, help='zoom level; number between  0 and  22 . Fractional zoom levels will be rounded to two decimal places.')
@click.option('--width', type=click.IntRange(1, 1280), default=1280, help='width of the image in pixels')
@click.option('--height', type=click.IntRange(1, 1280), default=1280, help='height of the image in pixels')
@click.option('--style', default='mapbox://styles/addxy/cim6u5lfi00k2cwm23exyzjim', help='mapbox://styles/{username}/{style_id}')
@click.option('--access_token', default='pk.eyJ1IjoiYWRkeHkiLCJhIjoiY2lsdmt5NjZwMDFsdXZka3NzaGVrZDZtdCJ9.ZUE-LebQgHaBduVwL68IoQ', help='Mapbox access token')
@click.option('--bearing', type=click.FLOAT, default=0, help='Rotates the map around its center. Number between 0 and 360.')
@click.option('--pitch', type=click.FLOAT, default=0, help='Tilts the map, producing a perspective effect. Number between 0 and 60.')
@click.option('--retina', is_flag=True, default=True, help='[boolean] If  @2x is added to request a retina 2x image will be returned')
@click.option('--attribution', is_flag=True, default=False, help='[boolean] Value controlling whether there is attribution on the image; defaults to  false')
@click.option('--logo', is_flag=True, default=False, help='[boolean] Value controlling whether there is a Mapbox logo on the image; defaults to  false')
@click.option('--upload', is_flag=True, default=False, help='[boolean] Upload to AWS S3')
@click.option('--delete', is_flag=True, default=False, help='[boolean] Delete PNG')
def cli(filename, **kwargs):
    """Command Line Interface."""
    validate_options(**kwargs)
    filename = get_filename(filename, **kwargs)
    create_png(filename, **kwargs)
    create_svg(filename, **kwargs)
    upload_aws_s3(filename, **kwargs)


def get_filename(filename, **kwargs):
    """Get filename."""
    if filename:
        return filename
    elif kwargs['location']:
        return kwargs['location']
    else:
        click.echo('[Error] Provide a --filename or --location \n')
        cli(['--help'])


def create_png(filename, **kwargs):
    """Connect to Mapbox Static API.

    https://www.mapbox.com/api-documentation/#retrieve-a-static-map-from-a-style

    Input: HTTP API parameters
    Output: raw Image
    """
    username, style_id = parse_style(kwargs['style'])
    params = {
        'access_token': kwargs['access_token'],
        'logo': str(kwargs['logo']).lower(),
        'attribution': str(kwargs['attribution']).lower()
    }
    lat, lng = get_latlng(**kwargs)
    url = 'https://api.mapbox.com/styles/v1/{username}/{style_id}/static/{lng},{lat},{zoom},{bearing},{pitch}/{width}x{height}{retina}'
    url = url.format(
        username=username,
        style_id=style_id,
        lng=lng,
        lat=lat,
        zoom=kwargs['zoom'],
        bearing=kwargs['bearing'],
        pitch=kwargs['pitch'],
        width=kwargs['width'],
        height=kwargs['height'],
        retina=('', '@2x')[kwargs['retina']]
    )
    with open('{}.png'.format(filename), 'w') as handle:
        response = requests.get(url, params=params, stream=True)

        for block in response.iter_content(1024):
            handle.write(block)


def get_latlng(**kwargs):
    """Latitude & Longitude."""
    if kwargs['location']:
        g = geocoder.google(kwargs['location'])
        if g.ok:
            click.echo('Successfuly Geocoded: {} {}'.format(g.address, g.latlng))
            return g.latlng
        else:
            click.echo('[Error] Could not geocode address: {} \n'.format(g.location))
            cli(['--help'])
    else:
        return kwargs['lat'], kwargs['lng']


def create_svg(filename, **kwargs):
    """Create SVG.

    Input: PNG <filename>
    Output: SVG <filename>
    """
    # ImageMagick 6.8.9 - convert
    # Usage: convert [options ...] file [ [options ...] file ...] [options ...] file
    subprocess.call(['convert', '{}.png'.format(filename), '{}.pnm'.format(filename)])

    # potrace 1.12. Transforms bitmaps into vector graphics.
    # <filename>                 - an input file
    # -s, --svg                  - SVG backend (scalable vector graphics)
    # -o, --output <filename>    - write all output to this file
    subprocess.call(['potrace', '--svg', '--output', '{}.svg'.format(filename), '{}.pnm'.format(filename)])
    os.remove('{}.pnm'.format(filename))

    # Remove extra files that are not needed anymore
    if kwargs['delete']:
        os.remove('{}.png'.format(filename))


def upload_aws_s3(filename, **kwargs):
    """Upload AWS S3 bucket."""
    if kwargs['upload']:
        filename = '{}.svg'.format(filename)
        s3_bucket = 'kratelabs.com'
        s3_path = 's3://{}/{}'.format(s3_bucket, filename)
        command = ['aws', 's3', 'cp', filename, s3_path, '--acl', 'public-read-write']
        print(' '.join(command))
        subprocess.call(command)
        print('https://{}.s3.amazonaws.com/{}'.format(s3_bucket, kwargs['upload']))


def parse_style(style):
    """Parse Style.

    Input: mapbox://styles/{username}/{style_id}
    Output: username, style_id
    """
    if 'mapbox://styles/' in style:
        style = style.split('mapbox://styles/', 1)[-1]
        username, style_id = style.split('/')
        return username, style_id


def validate_options(**kwargs):
    """Verrify user input options."""
    # Lat lng
    if not kwargs['location']:
        lat, lng = kwargs['lat'], kwargs['lng']

        if not lat and not lng:
            click.echo('[Error] Missing latitude & longitude \n')
            cli(['--help'])

        elif not lat:
            click.echo('[Error] Missing latitude \n')
            cli(['--help'])

        elif not lng:
            click.echo('[Error] Missing longitude \n')
            cli(['--help'])

        elif not -90 <= lat <= 90:
            click.echo('[Error] Latitude must be within -90 to 90 degrees. \n')
            cli(['--help'])

        elif not -180 <= lng <= 180:
            click.echo('[Error] Longitute must be within -180 to 180 degrees. \n')
            cli(['--help'])

    # Zoom Level
    if not kwargs['zoom']:
        click.echo('[Error] Missing zoom level \n')
        cli(['--help'])

    elif not 0 <= kwargs['zoom'] <= 22:
        click.echo('[Error] Zoom level must be within 0 to 22. \n')
        cli(['--help'])

    elif not 0 <= kwargs['pitch'] <= 60:
        click.echo('[Error] Pitch must be within 0 to 60 degrees. \n')
        cli(['--help'])

    elif not 0 <= kwargs['bearing'] <= 360:
        click.echo('[Error] Bearing must be within 0 to 360 degrees. \n')
        cli(['--help'])

if __name__ == '__main__':
    cli()
