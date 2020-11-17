#!/bin/bash
cd ..
docker build -t kuber/djangoauth -f Dockerfile .
docker save  kuber/djangoauth > myimage.tar
microk8s ctr image import myimage.tar
rm myimage.tar
