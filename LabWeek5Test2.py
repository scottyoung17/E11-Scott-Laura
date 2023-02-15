import random
import time
import argparse
import sys
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
from datetime import datetime
import adafruit_bme680

## lab 1 code
i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25
## lab 1 code end

## lab 3 code
reset_pin = None
# If you have a GPIO, its not a bad idea to connect it to the RESET pin
# reset_pin = DigitalInOut(board.G0)
# reset_pin.direction = Direction.OUTPUT
# reset_pin.value = False


# For use with a computer running Windows:
# import serial
# uart = serial.Serial("COM30", baudrate=9600, timeout=1)

# For use with microcontroller board:
# (Connect the sensor TX pin to the board/computer RX pin)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# For use with USB-to-serial cable:
# import serial
# uart = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)

# Create library object, use 'slow' 100KHz frequency!
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
#pm25 = PM25_I2C(i2c, reset_pin)

print("Found PM2.5 sensor, reading data...")
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
startTime = time.time()
endTime = startTime + 60

f = open("data.csv","w")
metaData = ["Time","PM 1.0", "PM 2.5", "PM 10"]
for entry in metaData:
    f.write(entry+',')
f.write('\n')
## lab 3 code end

## lab 5 code
print(sys.argv)

startTime = time.time()
runTime = int(sys.argv[1])
itime = startTime
## lab 5 code end


while itime < startTime + runTime: 
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    ##lab 1 code
    #print("Current Time =", currentTime)
    print("Current Time =", currentTime, "Temperature: %0.1f C" % bme680.temperature,"Gas: %d ohm" % bme680.gas,"Humidity: %0.1f %%" % bme680.relative_humidity,"Pressure: %0.3f hPa" % bme680.pressure, "Altitude = %0.2f meters" % bme680.altitude)
	#print("Gas: %d ohm" % bme680.gas);
	#print("Humidity: %0.1f %%" % bme680.relative_humidity);
	#print("Pressure: %0.3f hPa" % bme680.pressure);
	#print("Altitude = %0.2f meters" % bme680.altitude);

    ##lab 1 code end


    ##lab 3 code

    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Current Time = ", currentTime)
    print("---------------------------------------")
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    data = [currentTime,aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]]
    for entry in data:
        f.write(str(entry)+',')
    f.write('\n')
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")
    startTime = time.time()

    ##lab 5 code
    itime = time.time()
    idata = random.random()
    print(itime,idata)
    time.sleep(1)
    ##lab 5 code end

f.close()

    