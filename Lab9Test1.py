import RPi.GPIO as GPIO
import datetime

channel = GPIO.wait_for_edge(channel, GPIO_FALLING, timeout=5000)

def my_callback(channel):
    if GPIO.input(channel) == GPIO.LOW:
        print('\n▼  at ' + str(datetime.datetime.now()))


counts = 0
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.IN)
    GPIO.add_event_detect(6, GPIO.BOTH, callback=my_callback)

    GPIO.cleanup()

    counts = counts + 1
    print("Counts: ", counts)
    sleep(60)
 
