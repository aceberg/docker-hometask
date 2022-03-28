FROM ubuntu:20.04

CMD dd if=/dev/urandom of=/file.tmp bs=1024 count=1000000 oflag=direct status=progress > /mnt/dd-progress 2>&1