#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Renamer

The first version of grabimage neglected to zero-pad the frame numbers in filenames.
Oops. This is a quick fix for that problem.
"""

from os import listdir, rename

allfiles = listdir('.')
whalefiles = [whalefile for whalefile in allfiles if whalefile.startswith('whale')]
for whalefile in whalefiles:
    framenumber = int(whalefile[5:-4])
    rename(whalefile, "whale{:05d}.jpg".format(framenumber))
