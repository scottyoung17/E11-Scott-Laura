import RPi.GPIO as GPIO
import datetime
import random
import time
import argparse
import sys


def my_callback(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        global count
        count += 1
        print(time.time())




filename = sys.argv[1]
intTime = int(sys.argv[2])
f = open(filename+".csv","w")
metaData = ["Time","Count"]
for entry in metaData:
    f.write(entry+',')
f.write('\n')

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
##GPIO.setup(6, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(6, GPIO.FALLING, callback=my_callback)
try: 
    count = 0 
    startTime = time.monotonic()
    endTime = startTime + intTime

    while time.monotonic() < endTime:
        time.sleep(1)

        if time.monotonic() - startTime >= 10:
            print('Counts in last 10 seconds: ', count)
            data = [time.time,count]
            for idata in data:
                f.write(str(idata)+'')
            f.write('\n')
            count = 0
            startTime = time.monotonic()
except KeyboardInterrupt:
    GPIO.cleanup()
f.close()

 
