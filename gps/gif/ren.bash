#!/bin/bash
i=0
for f in $(ls -rt *.png); do
   i=$((i+1));
   mv "$f" "./ren/$(printf %06d $i).png";
done

