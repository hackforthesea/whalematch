#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
GrabImage

This is a quick-and-dirty script to grab still images from video streams.
It basically marches through frame-by-frame saving them as JPEGs.
"""

from cv2 import VideoCapture, imwrite
from argparse import ArgumentParser

def parse_command_line(raw_args=None):
    """
    Parse command-line arguments.

    Use the built-in Python argparse facility to parse the command-line
    arguments as well as construct and provide meaningful help and feedback
    should bad data be entered or help be requested. By doing this we'll
    automatically get a traditional usage message as well as a help
    response.

    Args:
        raw_args:   The arguments as obtained from the command line.
                    Normally this is left at None unless one wants to
                    load in values for unit testing.

    Returns:
        The input filename.
    """
    assert raw_args is None or isinstance(raw_args, list)
    # Use the Python argparser to parse command line input and provide
    # usage information and feedback should bad input be given or help
    # requested.
    default_filename = '../6AK2017_BlowholeCompilation_0929.mp4'

    parser = ArgumentParser(
        description="Grab still images from a video."
    )
    parser.add_argument(
        '--input', '-i', default=default_filename,
        nargs='?', const=default_filename, metavar="input_filename",
        help='Optional filename for input video file. '
        'Default: {0}'.format(default_filename)
    )
    args = parser.parse_args(raw_args)
    return args.input


def process_video(video_stream, prefix="whale"):
    """
    Process the input video stream, saving frames.

    Uses the OpenCV video capture functionality to step through frames of the
    input video and save them to disk.

    Args:
        video_stream:   The video stream, as produced by OpenCV VideoCapture.
        prefix:         A string prefix to use for filenames for stills.

    Returns:
        None.
    """
    count = 0
    success, image = video_stream.read()
    while success:
        imwrite("{}{:05d}.jpg".format(prefix, count), image)    
        success, image = video_stream.read()
        if success:
            print('Got frame: {}'.format(count))
        count += 1


if __name__ == '__main__':
    input_filename = parse_command_line()
    video_stream = VideoCapture(input_filename)
    process_video(video_stream)
