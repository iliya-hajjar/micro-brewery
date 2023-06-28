from flask import request
from flask_cors import CORS
from schema import Category, Supplier, Product, Base
from flask import Flask, jsonify, abort
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://someone:someone@db_warehouse:3306/warehouse'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

engine = create_engine("mysql+pymysql://someone:someone@db_warehouse:3306/warehouse", pool_recycle=3600)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


try:
    engine = create_engine("mysql+pymysql://someone:someone@db_warehouse:3306/warehouse", pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
except sqlalchemy.exc.OperationalError as e:
    session.rollback()
    print(e)


@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify(session.query(Product).all())


@app.route('/api/v1/product/<int:id>', methods=['GET'])
def get_product(id):
    return jsonify(session.query(Product).filter_by(id=id).first())


@app.route('/api/v1/product', methods=['POST'])
def set_product():
    try:
        data = request.get_json()
        product = Product(**data)
        session.add(product)
        session.commit()
        return jsonify({"status": 200, "id": product.id})
    except Exception as e:
        abort(400, e)


@app.route('/api/v1/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        data = request.get_json()
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        product.count = data['count']
        product.price = data['price']
        session.commit()
        return jsonify({"status": 200, "id": product.id})
    except Exception as e:
        abort(400, e)


@app.route('/api/v1/suppliers', methods=['GET'])
def get_suppliers():
    return jsonify(session.query(Supplier).all())


@app.route('/api/v1/supplier/<int:id>', methods=['GET'])
def get_supplier(id):
    return jsonify(session.query(Supplier).filter_by(id=id).first())


@app.route('/api/v1/supplier', methods=['POST'])
def set_supplier():
    try:
        data = request.get_json()
        supplier = Supplier(**data)
        session.add(supplier)
        session.commit()
        return jsonify({"status": 200, "id": supplier.id})
    except Exception as e:
        abort(400, 'Can not add new supplier !')


@app.route('/api/v1/categories', methods=['GET'])
def get_categories():
    return jsonify(session.query(Category).all())


@app.route('/api/v1/category/<int:id>', methods=['GET'])
def get_category(id):
    return jsonify(session.query(Category).filter_by(id=id).first())


@app.route('/api/v1/category', methods=['POST'])
def set_category():
    try:
        data = request.get_json()
        category = Category(**data)
        session.add(category)
        session.commit()
        return jsonify({"status": 200, "id": category.id})
    except Exception as e:
        abort(400, 'Can not add new category !')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
