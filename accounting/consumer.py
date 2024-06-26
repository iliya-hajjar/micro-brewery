import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accounting.settings")
django.setup()

from apps.transaction.models import Transaction, Payment


params = pika.URLParameters('')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='accounting')


def callback(ch, method, properties, body):
    print('Consume data from accounting')
    order_data = json.loads(body)

    if properties.content_type == 'order_created':
        payment_type = Payment.objects.get(id=order_data['payment_id'])
        transaction = Transaction.objects.create(order_id=order_data['order_id'],
                                                 amount=order_data["amount"], payment_type=payment_type,
                                                 user_id=order_data["user_id"])
        print(f'Transaction created {transaction.id}')


channel.basic_consume(queue='accounting', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
