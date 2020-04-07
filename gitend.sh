#!/bin/sh
git add -A
git commit -am "`%y%m%d%H%M`"
git push origin master
