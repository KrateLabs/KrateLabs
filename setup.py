#!/usr/bin/python
# coding: utf8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='kratelabs',
    version='0.1.0',
    description='Kratelab\'s helpful scripts for MapboxGL maps.',
    packages=['kratelabs'],
    entry_points={
        'console_scripts': [
            'svg = kratelabs.svg:cli'
        ]
    }
)
