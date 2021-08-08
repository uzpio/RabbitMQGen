import pika, os 
import json

credentials = pika.PlainCredentials('user', 'password')
parameters = pika.ConnectionParameters('hostname',
                                   5672,
                                   '/',
                                   credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='queue_name')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % json.loads(body))

channel.basic_consume(
    queue='queue_name', on_message_callback=callback, auto_ack=True)

channel.start_consuming()
