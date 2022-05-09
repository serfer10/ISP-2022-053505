#!/usr/bin/env python3.10
"""Setup serializer."""
from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='serializer_by_shinny',
    version='1.1',
    description='Application to serailize, deserialize and convert objects',
    author='Shiny',
    packages=['serialiser_modules', 'serializers'],
    scripts=['serial']
)