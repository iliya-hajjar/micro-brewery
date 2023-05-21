import pika, json
from schema import Order
from sales import session

params = pika.URLParameters('amqps://cjkiqrbh:M8HPj_fVGOwvCC4lMWYnol_9LHPeOrx1@woodpecker.rmq.cloudamqp.com/cjkiqrbh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='sales')


def callback(ch, method, properties, body):
    print('Consume data from accounting')
    data = json.loads(body)

    if properties.content_type == 'transaction_updated':
        order = Order.query.get(data['id'])
        order.transaction_id = data['transaction_id']
        session.commit()
        print('Order Created!')


channel.basic_consume(queue='sales', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
