#!/bin/sh
ffmpeg -framerate 30 -i img%06d.png -vcodec libx264 -pix_fmt yuv420p -r 60 out.mp4

