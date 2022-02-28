from gpiozero import Button, LED
from time import sleep
import Adafruit_DHT

button = Button(2)
led = LED(26)
sensor = Adafruit_DHT.DHT11
gpio = 4
while True:
    temperature,humidity = Adafruit_DHT.read(sensor,gpio)
    if humidity is not None and temperature is not None:
        print(temperature, humidity)
    else:
        print("No hay valores")
    sleep(3)
button.wait_for_press()
print("Has pulsao el botón")
led.on()
sleep(3)
led.off()

