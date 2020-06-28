#!/bin/sh
ffmpeg -r 5 -i SIR%04d.png -vf scale=1920x1080:flags=lanczos -vcodec libx264 -pix_fmt yuv420p -r 60 out.mp4

