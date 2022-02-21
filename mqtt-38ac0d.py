import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.3.3" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("house/main-light",tzone + ": " + loc_dt.strftime(fmt) )
import time



import datetime
import pytz

for tzone in ['America/Los_Angeles', 'America/New_York', 'Europe/London', 'Europe/Berlin', 'Asia/Dubai']:
    utc_dt = datetime.datetime.now()
    loc = pytz.timezone(tzone)
    loc_dt = utc_dt.astimezone(loc)
    fmt = '%Y-%m-%d %H:%M:%S'
    client.publish("DateTime/CONTINENT/CITY",tzone + ": " + loc_dt.strftime(fmt) )#publis
    time.sleep(1)
    print(tzone + ": " + loc_dt.strftime(fmt) )
