#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from argparse import ArgumentParser
from os import path
from subprocess import check_output
from sys import exit
try:
    import ffmpeg
except ImportError:
    print("Please install ffmpeg library! This can be acheived by running pip install -r requirements.txt.")
    exit(1)

def check_args(args):
    if not args.input:
        print("Please specifiy the input video URL.")
    if not args.output:
        print("Please specifiy the output video URL.")
    if not args.startime:
        print("Please specifiy the start of the GIF.")
    if not args.endtime:
        print("Please specifiy the end of the GIF.")
    return args
    
def check_ffmpeg_version():
    """
    enure the version of ffmpeg is >= 4.0
    
    """
    version = check_output(r"ffmpeg -version | grep '^ffmpeg\sversion\s[0-9]' | cut -d ' ' -f 3", shell=True).decode("utf-8").strip("\n")
    if int(version.split(".")[0]) < 4:
        print("Please install an ffmpeg version >= 4.0")
        exit(1)
        

def check_directory(directory):
    """
    ensure the directory specified exists in the filesystem.
    Args:
        directory: the output directory of the GIF.

    """
    if path.exists(directory):
        if path.isdir(directory):
            return directory   

def convert_to_gif(input, output, startime, endtime):
    """

    Slice the specified video by the startime and endtime and convert it to a GIF.
    
    Args:
        input: the url of the video.
        ouput: the output directory of the video.
        starttime: the start of the GIF.
        endtime: the end of the GIF.
    
    Return:
        The GIF data

    """
    
    ffmpeg_in = ffmpeg.input(input)

    (
        ffmpeg
        .concat(
            ffmpeg_in.trim(start=startime, end=endtime),
        )
        .output("{}/test.gif".format(output))
        .run()

    )

def main():
    parser = ArgumentParser(prog="gifpy", description="A simple CLI to create a GIF from a video.", add_help=True)
    parser.add_argument("-i", "--input", action="store", dest="input", help="Input Video URL")
    parser.add_argument("-o", "--output",  action="store", dest="output", type=lambda d:check_directory(d), help="Output Video URL")
    parser.add_argument("-s", "--startime", action="store", dest="startime", type=str , help="Start time of the clip (e.g. 1:00)")
    parser.add_argument("-e", "--endtime", action="store", dest="endtime", type=str, help="End time of the clip (e.g. 1:40)")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s {version}".format(version="__version__"), help="Show the version of the program")
    args = parser.parse_args()
    checked_args = check_args(args)
    check_ffmpeg_version()
    convert_to_gif(checked_args.input, checked_args.output, checked_args.startime, checked_args.endtime)

            
if __name__ == "__main__":
    main()