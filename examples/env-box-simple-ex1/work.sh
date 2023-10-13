#!/bin/bash




cd src
./exec.sh
mv -f example-1.png ../example.png

cd ..


zip -r src.zip src/
