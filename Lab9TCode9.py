import RPi.GPIO as GPIO
from datetime import datetime
from datetime import date
import random
import csv
import time
import argparse
import sys


def my_callback(channel):
    print(time.time())
    global count
    count += 1


runTime= int(sys.argv[1])
interval = int(sys.argv[2])
filename = sys.argv[3]
file = open(filename + '.csv','w')
writer = csv.writer(file)
metadata= ['Time','Counts']
writer.writerow(metadata)
count = 0
secCount = 0

startTime = time.time()
itime = startTime

GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.IN)
GPIO.add_event_detect(6,GPIO.FALLING, callback = my_callback)


while itime < (startTime + runTime):
    time.sleep(interval)
    data = [time.time(),count]
    writer.writerow(data)
    itime = time.time()
    count = 0
file.close()

