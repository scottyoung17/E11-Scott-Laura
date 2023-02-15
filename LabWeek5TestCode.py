import random
import time
import argparse
import sys

print(sys.argv)

startTime = time.time()
runTime = int(sys.argv[1])
itime = startTime

while itime < startTime + runTime: 
    itime = time.time()
    idata = random.random()
    print(itime,idata)
    time.sleep(1)
