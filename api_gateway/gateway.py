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
    response = requests.request("POST", "http://host.docker.internal:8004/signup",
                                headers={'Content-Type': 'application/json'},
                                data=payload_signup)
    if response.status_code == 200:
        return {"status": response.status_code}
    else:
        return {"status": 400}


@server.route('/category/<int:id>', methods=['GET'], strict_slashes=False)
def get_category(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://host.docker.internal:8001/api/v1/category/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/category', methods=['POST'], strict_slashes=False)
def set_category():
    if request.method == 'POST':
        access, err = validate.token(request)

        if err:
            return err
        try:
            data = request.get_json()
            response = requests.request("POST", "http://host.docker.internal:8001/api/v1/category",
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(data))
            return response
        except Exception as e:
            abort(400, 'Can not add new category !')
    else:
        abort(400, 'Wrong method')


@server.route('/suppliers', methods=['GET'], strict_slashes=False)
def get_suppliers():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://host.docker.internal:8001/api/v1/suppliers").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/supplier/<int:id>', methods=['GET'], strict_slashes=False)
def get_supplier(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://host.docker.internal:8001/api/v1/supplier/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/supplier', methods=['POST'], strict_slashes=False)
def set_supplier():
    if request.method == 'POST':
        access, err = validate.token(request)

        if err:
            return err
        try:
            data = request.get_json()
            response = requests.request("POST", "http://host.docker.internal:8001/api/v1/supplier",
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(data)).json()
            return response
        except Exception as e:
            abort(400, 'Can not add new category !')
    else:
        abort(400, 'Wrong method')


@server.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://host.docker.internal:8001/api/v1/products").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/product/<int:id>', methods=['GET'], strict_slashes=False)
def get_product(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://host.docker.internal:8001/api/v1/product/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/product', methods=['POST'], strict_slashes=False)
def set_product():
    if request.method == 'POST':
        access, err = validate.token(request)

        if err:
            return err
        try:
            data = request.get_json()
            response = requests.request("POST", "http://host.docker.internal:8001/api/v1/product",
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(data)).json()
            return response
        except Exception as e:
            abort(400, 'Can not add new category !')
    else:
        abort(400, 'Wrong method')


@server.route('/order/<int:id>', methods=['GET'], strict_slashes=False)
def get_order(id):
    access, err = validate.token(request)

    if err:
        return err
    try:
        response = requests.request("GET", f"http://host.docker.internal:8001/api/v1/order_detail/{id}").json()
        return jsonify(response)
    except Exception as e:
        abort(400, 'Can not add new category !')


@server.route('/order', methods=['POST'], strict_slashes=False)
def set_order():
    if request.method == 'POST':
        access, err = validate.token(request)

        if err:
            return err
        try:
            data = request.get_json()
            response = requests.request("POST", "http://host.docker.internal:8001/api/v1/order_detail",
                                        headers={'Content-Type': 'application/json'},
                                        data=json.dumps(data)).json()
            return response
        except Exception:
            abort(400, 'Can not add new category !')
    else:
        abort(400, 'Wrong method')


if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0")
