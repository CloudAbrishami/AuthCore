#!/bin/bash
cd ..
docker build -t authcordevelop -f Dockerfile .
docker run -it --rm -v $PWD/AuthJwt:/src -p 8000:8000 authcordevelop