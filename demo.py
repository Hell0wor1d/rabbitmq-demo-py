#!/usr/bin/env python
__author__ = 'kev7n'

import pika
import logging
from datetime import *

logging.basicConfig()

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
for i in range(0, 10):
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World! Num: ' + str(i) + ', Time: ' + str(datetime.now()))
print " [x] Sent 'Hello World!'"
connection.close()