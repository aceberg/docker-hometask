FROM ubuntu:20.04

RUN apt update && apt -y install python3-pip && pip3 install prometheus_client

COPY progress.py .

CMD python3 progress.py