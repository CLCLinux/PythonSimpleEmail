#!/usr/bin/python

# Do not name this file email.py or have email.pyc in the directory
# This will not run!! you will get Import Errors
#
import os
import sys
import smtplib
# for guessing MIME type based on the file name extension
import mimetypes

from email import Encoders
from email.Message import Message
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# open a plain text file for editing assuming only asci char.
#
# Create a text/plain message
#
fromaddr ='***@gmail.com'
toaddrs = '****@gmail.com'
msg = 'test 123  got it !!!'
username='*****@gmail.com'
password='******'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit
