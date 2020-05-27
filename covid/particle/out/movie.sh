#!/bin/sh
ffmpeg -r 5 -i SIR%04d.png -vcodec libx264 -pix_fmt yuv420p -r 60 out.mp4

