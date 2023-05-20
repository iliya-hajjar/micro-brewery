import json
from flask import request
from flask_cors import CORS
from schema import Order, OrderDetails, Base
from flask import Flask, jsonify, abort
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://someone:someone@db/sales'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

engine = create_engine("mysql+pymysql://someone:someone@db/sales")
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


@app.route('/api/v1/order/<int:id>', methods=['PUT'], strict_slashes=False)
def update_order(id):
    try:
        data = request.get_json()
        order = session.query(Order).filter_by(id=id).first()
        order.transaction_id = data['transaction_id']
        session.commit()
        return jsonify(order)
    except Exception as e:
        abort(400, 'Can not update order !')


@app.route('/api/v1/order_detail', methods=['POST'], strict_slashes=False)
def set_order():
    try:
        data = request.get_json()
        order = Order(user_id=data.pop('user_id', None))
        session.add(order)
        session.commit()
        data['order_id'] = order.id
        order_details = OrderDetails(**data)
        session.add(order_details)
        session.commit()
        return jsonify({"status": 200, "order_details_id": order_details.id})
    except Exception as e:
        abort(400, 'Can not add new order !')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
