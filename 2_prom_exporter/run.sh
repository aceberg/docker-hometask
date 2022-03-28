#!/bin/bash

DISK_PATH="/dev/mapper/vg0-sys"
IOPS_LIMIT=10

printf "\n ### Build images\n"
docker build -t dds ./dd-server/
docker build -t ddc ./dd-client/

printf "\n ### Stop and remove containers if they exist\n"
docker stop dds || true && docker rm dds || true
docker stop ddc || true && docker rm ddc || true

printf "\n ### Run new containers\n"
docker run --name dds -v /tmp/docker-dd:/mnt --device-write-iops="$DISK_PATH:$IOPS_LIMIT" dds &
sleep 5
docker run --name ddc -v /tmp/docker-dd:/mnt -p 9999:9999 ddc