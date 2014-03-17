#!/usr/bin/env python

from setuptools import setup


setup(
    name='Distutils',
    version='1.0',
    description='VT100 Animatior',
    author='Chris Sinchok',
    author_email='chris@sinchok.com',
    url='http://github.com/csinchok/vt100-animator',
    py_modules=['vt100'],
    entry_points={
        "console_scripts": [
            "vt100-animator = vt100:main"
        ]
    }
)
