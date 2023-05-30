!/opt/homebrew/bin/zsh
ffmpeg -r 6 -i %06d.png -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -vcodec libx264 -pix_fmt yuv420p out.mp4
