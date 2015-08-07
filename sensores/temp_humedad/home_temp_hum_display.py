# home_temp_hum_display.py.py
#
# This is an project for using the Grove OLED Display and the Grove DHT Sensor from the GrovePi starter kit
# 
# In this project, the Temperature and humidity from the DHT sensor is printed on the DHT sensor
'''
## License
 GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
 Copyright (C) 2015 Dexter Industries

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''

from grovepi import *
from datetime import datetime
from kafka import SimpleProducer, KafkaClient
import json

dht_sensor_port = 7		# Connect the DHt sensor to port 7
contador = 0


def create_json():
    """Returns a JSON data structure with sensor data."""
    
    # Almacenamos el valor de la hora actual
    now = datetime.now().strftime("%H:%M:%S")

    # Generamos la estructura de datos de tipo dictionary
    data = []
    data.append({"timestamp":now,"device":"raspberrypi","location":"etxea","tempvalue":temp,"humidityvalue":hum})
    sensor_json = json.dumps(data)

    # Save JSON to data.txt file:
    save_json(sensor_json)

    # Send JSON to Apache-Kafka:
    send_json_kafka(sensor_json)

    return sensor_json

def save_json(data):
    """Stores JSON data in a file.Everytime a new JSON is generated data.txt is overwritten."""
    
    file = open("data.txt", "w")
    file.write(data)
    file.close()

def send_json_kafka(data):
    """Sends JSON data to Apache-Kafka's "idi_raspberrypi" topic."""
    
    kafka = KafkaClient('lana-kafka01:9092')
    producer = SimpleProducer(kafka)
    producer.send_messages(b'idiraspberrypi', data)

while True:
	try:
		contador +=1
		[ temp,hum ] = dht(dht_sensor_port,1)		#Get the temperature and Humidity from the DHT sensor
		#print "temp =", temp, "C\thumidity =", hum,"%" 	

		# Every 10s a JSON containing sensor data is generated and stored in data.txt file
		if contador==30:
			contador = 0
			sensor_data = create_json();

			#Print returned JSON:
			print(sensor_data)


	except (IOError,TypeError) as e:
		print "Error"
