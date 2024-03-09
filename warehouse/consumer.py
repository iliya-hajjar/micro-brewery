import pika, json
from warehouse import session
from schema import Product

params = pika.URLParameters('')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='warehouse')


def callback(ch, method, properties, body):
    print('Consume data from sales')
    data = json.loads(body)

    if properties.content_type == 'order_confirmed':
        product = session.query(Product).filter_by(id=data['product_id']).first()
        if product:
            product.reserved_product -= data['product_count']
            session.commit()
            print('product amount updated!')
    elif properties.content_type == 'reserve_product':
        print("Reserving product!")
        product = session.query(Product).filter_by(id=data['product_id']).first()
        if product:
            product.count -= data['product_count']
            product.reserved_product += data['product_count']
            session.commit()
            print("Product reserved!")


channel.basic_consume(queue='warehouse', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
