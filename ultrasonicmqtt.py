import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
broker_address = "192.168.0.160"
client = mqtt.Client("P1")
client.connect(broker_address)

GPIO.setmode(GPIO.BCM)
TRIG=4
ECHO=17
print('DIstancia medida en progreso lmao')

while True:

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)

    print("El sensor se est'a agjustando")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration*17150

    distance =round(distance,2)


    print("Distance",distance, "cm")
    
    client.publish("Medidas/Distancia",distance)

    GPIO.cleanup()

