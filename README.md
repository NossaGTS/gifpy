# gifpy
gifpy is a simple CLI to create GIFs using ffmpeg.

## Installation
Install gifpy:
    python3 setup.py install
You will also need to install ffmpeg:

On GNU/LINUX Debian systems:
    apt-get install ffmpeg
On GNU/LINUX Arch systems:
    pacman -S ffmpeg
On OS X, you can use homebrew to install ffmpeg:
    brew install ffmpeg

## Usage
python gifpy.py -i test.mp4 -o ~/Desktop/ -s 2 -e 4