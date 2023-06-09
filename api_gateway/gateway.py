import requests
import json
from flask import Flask, request, jsonify, abort
from utils import validate, access

server = Flask(__name__)


@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)
    token, err = access.login(request)

    if not err:
        return token
    else:
        return err


@server.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    payload_signup = json.dumps({
        "email": data['email'],
        "password": data['password'],
    })
    response = requests.request("POST", "http://auth:5000/signup",
                                headers={'Content-Type': 'application/json'},
                                data=payload_signup)
    if response.status_code == 200:
        return {"status": response.status_code}
    else:
        return {"status": 400}


@server.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://warehouse:5000/api/v1/categories").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/category/<int:id>', methods=['GET'], strict_slashes=False)
def get_category(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://warehouse:5000/api/v1/category/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get category !')


@server.route('/category', methods=['POST'], strict_slashes=False)
def set_category():
    access, err = validate.token(request)

    if err:
        return err
    try:
        data = request.get_json()
        response = requests.request("POST", "http://warehouse:5000/api/v1/category",
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(data)).json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/suppliers', methods=['GET'], strict_slashes=False)
def get_suppliers():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://warehouse:5000/api/v1/suppliers").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get suppliers !')


@server.route('/supplier/<int:id>', methods=['GET'], strict_slashes=False)
def get_supplier(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://warehouse:5000/api/v1/supplier/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get supplier !')


@server.route('/supplier', methods=['POST'], strict_slashes=False)
def set_supplier():
    access, err = validate.token(request)

    if err:
        return err
    try:
        data = request.get_json()
        response = requests.request("POST", "http://warehouse:5000/api/v1/supplier",
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(data)).json()
        return response
    except Exception as e:
        abort(400, 'Can not add new supplier !')


@server.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://warehouse:5000/api/v1/products").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get products !')


@server.route('/product/<int:id>', methods=['GET'], strict_slashes=False)
def get_product(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://warehouse:5000/api/v1/product/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get product !')


@server.route('/product', methods=['POST'], strict_slashes=False)
def set_product():
    access, err = validate.token(request)

    if err:
        return err
    try:
        data = request.get_json()
        response = requests.request("POST", "http://warehouse:5000/api/v1/product",
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(data)).json()
        return response
    except Exception as e:
        abort(400, 'Can not add new product !')


@server.route('/product/<int:product_id>', methods=['PUT'], strict_slashes=False)
def update_product(product_id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        data = request.get_json()
        response = requests.request("PUT", f"http://warehouse:5000/api/v1/product/{product_id}",
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(data)).json()
        return response
    except Exception:
        abort(400, 'Can not update product !')


@server.route('/order/<int:id>', methods=['GET'], strict_slashes=False)
def get_order(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://sales:5000/api/v1/order_detail/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get order !')


@server.route('/orders', methods=['GET'], strict_slashes=False)
def get_orders():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://sales:5000/api/v1/order_details").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get order !')


@server.route('/order', methods=['POST'], strict_slashes=False)
def set_order():
    access, err = validate.token(request)

    if err:
        return err
    try:
        data = request.get_json()
        response = requests.request("POST", "http://sales:5000/api/v1/order_detail",
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(data)).json()
        return response
    except Exception:
        abort(400, 'Can not add new order !')


@server.route('/payment', methods=['POST'], strict_slashes=False)
def set_payment():
    access, err = validate.token(request)

    if err:
        return err
    try:
        data = request.get_json()
        response = requests.request("POST", "http://accounting:8000/api/v1/transaction/payments",
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(data)).json()
        return response
    except Exception:
        abort(400, 'Can not add new payment !')


@server.route('/payment', methods=['GET'], strict_slashes=False)
def get_payment():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://accounting:8000/api/v1/transaction/payments").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get payment !')


@server.route('/transaction/<string:tx_id>', methods=['PUT'], strict_slashes=False)
def update_transaction(tx_id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        data = request.get_json()
        response = requests.request("PUT", f"http://accounting:8000/api/v1/transaction/transactions/{tx_id}",
                                    headers={'Content-Type': 'application/json'},
                                    data=json.dumps(data)).json()
        return response
    except Exception:
        abort(400, 'Can not update transaction !')


@server.route('/transactions', methods=['GET'], strict_slashes=False)
def get_transactions():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://accounting:8000/api/v1/transaction/transactions").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not get transaction !')


if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0")
