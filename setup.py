#!/usr/bin/python3
# -*- encoding: utf-8 -*-
try:
    from distutils.core import setup
except:
    from setuptools import setup

__long_description__ = """ GifPy is a simple CLI tool that generates a GIFs from a video.  
                           Gifpy works with a URL or PATH to a video. Simple provide the path/urland 
                           the start and end time of the frames you would like to convert to a gif """


setup(
    name                    = "gifpy",
    version                 = "0.1a",
    description             = "CLI tool to easy generate a GIF from a video.",
    long_description        = __long_description__,
    url                     = "https://www.github.com/",
    packages                = ["gifpy"],
    package_dir             = {"gifpy": "."},
    package_data            = {"gifpy": ['setup.py', 'test.py']},
    license                 = "MIT",
    py_modules              = ["gifpy"],
    dist_requires                = ["ffmpeg-python",],
)