# Detects motion, triggers Buzzer, LED and Relay, takes picture from RPi Camera, sends as attachment via Gmail
# http://www.dexterindustries.com/GrovePi/projects-for-the-raspberry-pi/whos-at-the-door/

# GrovePi + Ultrasonic Ranger + Buzzer + Switch + Relay + LED + RPi Camera
# http://www.seeedstudio.com/wiki/Grove_-_Ultrasonic_Ranger
# http://www.seeedstudio.com/wiki/Grove_-_Buzzer
# http://www.seeedstudio.com/wiki/Grove_-_Switch(P)
# http://www.seeedstudio.com/wiki/Grove_-_Solid_State_Relay
# http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit
# http://www.raspberrypi.org/camera

'''
## License
 GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
 Copyright (C) 2015  Dexter Industries

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

'''
Etxahun: Hay que habilitar el  accesso de aplicaciones menos seguras en la cuenta de e-mail emisora:

	https://www.google.com/settings/security/lesssecureapps

	Y pulsaremos en ACTIVAR.
'''


import grovepi
# Import smtplib for the actual sending function
import smtplib, string, subprocess, time, mimetypes

# Here are the email package modules we'll need
import email.mime.application

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from subprocess import call

import sys

print "System Working"
#sensor = X

SMTP_USERNAME = 'xxxxxxxx@gmail.com'  # Mail id of the sender
SMTP_PASSWORD = 'yyyyyyy'  # Pasword of the sender
SMTP_RECIPIENT = 'zzzzzzzz@gmail.com' # Mail id of the reciever
SMTP_SERVER = 'smtp.gmail.com'  # Address of the SMTP server
SSL_PORT = 465

# Create the container (outer) email message
TO = SMTP_RECIPIENT
FROM = SMTP_USERNAME
msg = MIMEMultipart()
msg.preamble = 'Rpi Sends image'

# Attach the image
fp = open('nextel.png', 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

# Send the email via Gmail
print "Sending the mail"
server = smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT)
server.login(SMTP_USERNAME, SMTP_PASSWORD)
server.sendmail(FROM, [TO], msg.as_string())
server.quit()
print "Mail sent"
