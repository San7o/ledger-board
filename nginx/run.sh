#!/bin/sh

docker build -t nginx-reverse-proxy .
docker run -d -p 80:80 -v nginx.conf:/etc/nginx/nginx.cong nginx-reverse-proxy
