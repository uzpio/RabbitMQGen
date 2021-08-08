import pika
import random
import json

items = ('Bilbao', "Torino", "Wroclaw", "Mumbai", "Kansas", "Paris")

def rabbitsend(qname):
    rows = [[random.randrange(10000000,99999999), random.randrange(0,10), i/2, i*0.678, random.random(), random.choice(items)] for i in range(random.randrange(50,600))]
    i = random.randrange(50,600)
    message = {'Random': random.randrange(10000000,99999999), 'P': random.randrange(0,10), "P/2": i/2, "P*0.678": i*0.678, "rand": random.random(), "City": random.choice(items)}
    print(message)
    credentials = pika.PlainCredentials('user', 'password')
    properties = pika.BasicProperties(content_encoding='utf-8')
    parameters = pika.ConnectionParameters('hostname',
                                   5672,
                                   '/',
                                   credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=qname, durable=True)
    channel.basic_publish(exchange='',
                        routing_key=qname,
                        body=json.dumps(message),
                        properties=properties)
    connection.close()


rabbitsend('queue_name')
