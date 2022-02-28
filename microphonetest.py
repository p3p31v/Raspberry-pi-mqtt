from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

rec = 15

GPIO.setup(rec,GPIO.OUT)
GPIO.output(rec,0)

def record():
    print("Grabando 10 segundos")
    GPIO.output(rec,1)
    sleep(10)
    GPIO.output(rec,0)
    sleep(5)

record()

