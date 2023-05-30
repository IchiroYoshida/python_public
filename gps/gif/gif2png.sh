#!/bin/bash
for f in *.gif
do
  convert $f ${f%.*}.png
done

