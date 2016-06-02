#!/usr/bin/python
# coding: utf8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    REQUIRES = f.readlines()

setup(
    name='kratelabs',
    version='0.2.1',
    author='Denis Carriere',
    author_email='carriere.denis@gmail.com',
    url='https://github.com/KrateLabs/KrateLabs-CLI',
    description='Kratelab\'s helpful scripts for MapboxGL maps.',
    packages=['kratelabs'],
    install_requires=[REQUIRES],
    entry_points={
        'console_scripts': [
            'kratelabs = kratelabs.cli:cli'
        ]
    }
)
