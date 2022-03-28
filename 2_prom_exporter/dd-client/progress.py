#!/bin/python3

import prometheus_client
import time

PATH_TO_FILE = "/mnt/dd-progress"
SERVER_PORT = 9999
UPDATE_PERIOD = 5
DD_PROGRESS = prometheus_client.Gauge('dd_progress',
                                       'Progress of file copying with dd',
                                       ['resource_type'])

def get_dd_progress():
  f = open(PATH_TO_FILE, "r")
  for line in f:
    pass
  last_line = line.split()
  f.close() 
  #print(last_line)
  size = last_line[0]
  time = last_line[7]
  speed = last_line[9]
  return(size,time,speed)

if __name__ == '__main__':
  prometheus_client.start_http_server(SERVER_PORT)
  
while True:
  DD_PROGRESS.labels('Size (bytes)').set(get_dd_progress()[0])
  DD_PROGRESS.labels('Time (sec)').set(get_dd_progress()[1])
  DD_PROGRESS.labels('Speed (kB/s)').set(get_dd_progress()[2])
  time.sleep(UPDATE_PERIOD)