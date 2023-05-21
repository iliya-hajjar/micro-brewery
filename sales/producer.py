import pika, json

params = pika.URLParameters('amqps://cjkiqrbh:M8HPj_fVGOwvCC4lMWYnol_9LHPeOrx1@woodpecker.rmq.cloudamqp.com/cjkiqrbh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='accounting', body=json.dumps(body), properties=properties)


def publish_warehouse(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='warehouse', body=json.dumps(body), properties=properties)
