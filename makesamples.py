import argparse
import os
import sys
import shutil
import random
import time

#import argparser
from PIL import Image, ImageFilter

def _make_argparse():
    parser = argparse.ArgumentParser(description="For each still in a folder of stills from a movie clip (use grabimages.py),"
                                                  "make one random 75x75 (200x200 images resized) sample and save it in another folder."
                                                  "!!!You still need manual inspection that you don't have blowholes!!!")
    parser.add_argument("-p","--path",
            type=str,
            help="The folder of stills you with to convert")

    parser.add_argument("--destination",
            default="",
            type=str,
            help="The distination of the samples. If empty, use the pattern {path + '_samples'} or if path ends in '_raw', replace with '_samples'")

    return parser

def main(argv=None):
    if not argv:
        argv = _make_argparse().parse_args(sys.argv[1:])

    #print(os.path.abspath(__file__))
    # For each file
    for root, dirs, files in os.walk(argv.path):
        #print(root)
        #print(dirs)
        #print(files)

        for f in files:
            im = Image.open(os.path.join(root,f),'r')
            width, height = im.size

            #L,T,R,B
            left = random.randint(0,width-200)
            top = random.randint(0,height-200)
            #print(left)
            #print(top)

            tile = im.crop((left,top,left+200,top+200))
            resized_tile = tile.resize((75,75))
            basename = os.path.basename(argv.path)
            if not argv.destination:
                dest = os.path.join(os.path.split(argv.path)[0], basename + "_samples",f)
            elif not argv.destination and argv.path.endswith("_raw"):
                dest = os.path.join(os.path.split(argv.path)[0], basename[:basename.index('_raw')] + "_samples",f)
            else:
                dest = argv.destination

            try:
                os.makedirs(os.path.split(dest)[0])
            except:
                pass

            #print(dest)
            resized_tile.save(dest, format="jpeg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
