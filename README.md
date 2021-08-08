# RabbitMQ message generator and receiver
Here you can find data generator that will publish random data on selected rabbitmq queue and data receiver, that will receive and print incoming messages on received rabbitmq queue

In generate.py you need to modify:
credentials = pika.PlainCredentials('user', 'password') - and replace with your user and password
parameters = pika.ConnectionParameters('hostname', - and replace with your hostname (can be localhost)
rabbitsend('queue_name') - and replace with queue name

In receive.py
credentials = pika.PlainCredentials('user', 'password') - and replace with your user and password
parameters = pika.ConnectionParameters('hostname', - and replace with your hostname (can be localhost)
