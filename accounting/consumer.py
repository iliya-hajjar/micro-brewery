import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accounting.settings")
django.setup()

from apps.transaction.models import Transaction, Payment


params = pika.URLParameters('amqps://cjkiqrbh:M8HPj_fVGOwvCC4lMWYnol_9LHPeOrx1@woodpecker.rmq.cloudamqp.com/cjkiqrbh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='accounting')


def callback(ch, method, properties, body):
    print('Consume data from accounting')
    order_data = json.loads(body)

    if properties.content_type == 'order_created':
        payment_type = Payment.objects.get(id=order_data['payment_id'])
        transaction = Transaction.objects.create(order_id=order_data['order_id'],
                                                 amount=order_data["amount"], payment_type=payment_type)
        print(f'Transaction created {transaction.id}')


channel.basic_consume(queue='accounting', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
