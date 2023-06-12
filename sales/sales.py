import json
import requests
from flask import request
from flask_cors import CORS
from schema import Order, OrderDetails, Base
from flask import Flask, jsonify, abort
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from producer import publish, publish_warehouse


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://someone:someone@sales_db:3306/sales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

engine = create_engine("mysql+pymysql://someone:someone@sales_db:3306/sales")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/api/v1/order_details', methods=['GET'], strict_slashes=False)
def get_orders():
    return jsonify(session.query(OrderDetails).all())


@app.route('/api/v1/order_detail/<int:id>', methods=['GET'], strict_slashes=False)
def get_order(id):
    order_data = json.loads(json.dumps(session.query(OrderDetails).filter_by(id=id).first().order, default=Order.to_dict))
    order_details_data = json.loads(json.dumps(session.query(OrderDetails).filter_by(id=id).first(), default=OrderDetails.to_dict))
    order_details_data['order'] = order_data
    return jsonify(order_details_data)


@app.route('/api/v1/order/<string:order_id>', methods=['PUT'], strict_slashes=False)
def update_order(order_id):
    order = session.query(Order).filter_by(id=order_id).first()
    order_detail = session.query(OrderDetails).filter_by(order_id=order_id).first()
    try:
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        order.transaction_id = order.transaction_id
        session.commit()
        publish_warehouse('order_confirmed', {'product_count': order_detail.product_count, 'product_id': order_detail.product_id})
        return jsonify({"status": 200})
    except Exception as e:
        abort(400, e)


@app.route('/api/v1/order_detail', methods=['POST'], strict_slashes=False)
def set_order():
    try:
        data = request.get_json()
        product = requests.get(f'http://warehouse:5000/api/v1/product/{data["product_id"]}')
        if product.status_code == 200:
            if product.json()['reserved_product'] - data['product_count'] <= product.json()['count']:
                order = Order(user_id=data.pop('user_id', None), amount=data.pop('amount', None))
                payment_id = data.pop('payment_id', None)
                session.add(order)
                session.commit()
                data['order_id'] = order.id
                order_details = OrderDetails(**data)
                session.add(order_details)
                session.commit()
                publish('order_created', {'order_id': order.id, 'amount': order.amount,
                                          'user_id': order.user_id, 'payment_id': payment_id})
                publish_warehouse('reserve_product', {'product_count': data['product_count'],
                                                      'product_id': data["product_id"]})
                return jsonify({"status": 200, "order_details_id": order_details.id})
            else:
                return jsonify({"status": 200, "info": "this item with this amount does not exist!"})
        else:
            abort(400, 'Can not add new order !')
    except Exception as e:
        abort(400, 'Can not add new order !')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
