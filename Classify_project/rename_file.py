import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required = True,
	help = "source")
ap.add_argument("-n", "--name", required = True,
        help = "name")
args = vars(ap.parse_args())

for count, filename in enumerate(os.listdir(args["source"]), 1):
    dst = args["name"] + "_" + str(count) + ".png"
    src = args["source"] + filename
    dst = args["source"] + dst

    os.rename(src,dst)
