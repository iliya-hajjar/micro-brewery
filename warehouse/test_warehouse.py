import requests
import json


headers = {
  'Content-Type': 'application/json'
}


def test_supplier_pass_post():
    num_of_columns = 5
    data = {
        "name": "amazon",
        "address": "sssssssssssssssss",
        "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://warehouse:5000/api/v1/supplier", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://warehouse:5000/api/v1/supplier/{response_post.json()["id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns == len(response_data)
    assert all([False for key in response_data.keys() if key not in ["address", "id", "name", "create_at", "category_id"]])


def test_supplier_fail_post():
    num_of_columns = 6
    data = {
        "name": "amazon",
        "address": "sssssssssssssssss",
        "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://warehouse:5000/api/v1/supplier", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://warehouse:5000/api/v1/supplier/{response_post.json()["id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns != len(response_data)
    assert not all([False for key in ["address", "id", "name", "create_at", "category_id", "problem"] if key not in response_data.keys()])


def test_product_pass_post():
    num_of_columns = 5
    data = {
      "name": "rozhe",
      "price": 10,
      "brand": "fecewrgw",
      "count": 10,
      "location": "Aaaaaaaaaaaaaaaa",
      "description": "qqqqqqqqqq",
      "supplier_id": 1,
      "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://warehouse:5000/api/v1/product", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://warehouse:5000/api/v1/supplier/{response_post.json()["id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns == len(response_data)
    assert not all([False for key in ["address", "id", "name", "create_at", "category_id", "problem"] if key not in response_data.keys()])


def test_product_fail_post():
    num_of_columns = 6
    data = {
      "name": "rozhe",
      "price": 10,
      "brand": "fecewrgw",
      "count": 10,
      "location": "Aaaaaaaaaaaaaaaa",
      "description": "qqqqqqqqqq",
      "supplier_id": 1,
      "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://warehouse:5000/api/v1/product", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://warehouse:5000/api/v1/supplier/{response_post.json()["id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns != len(response_data)
    assert not all([False for key in ["address", "id", "name", "create_at", "category_id", "problem"] if key not in response_data.keys()])


def test_product_pass_put():
    num_of_columns = 2
    data = {
      "name": "rozhe",
      "price": 10,
      "brand": "fecewrgw",
      "count": 10,
      "location": "Aaaaaaaaaaaaaaaa",
      "description": "qqqqqqqqqq",
      "supplier_id": 1,
      "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://warehouse:5000/api/v1/product", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_data = response_post.json()
    response_post = requests.request("PUT", f"http://warehouse:5000/api/v1/product/{response_data['id']}", headers=headers, data=payload)
    assert response_post.status_code == 200
    assert num_of_columns == len(response_data)
    assert all([False for key in response_data.keys() if key not in ["id", "status"]])


def test_product_fail_put():
    num_of_columns = 6
    data = {
      "name": "rozhe",
      "price": 10,
      "brand": "fecewrgw",
      "count": 10,
      "location": "Aaaaaaaaaaaaaaaa",
      "description": "qqqqqqqqqq",
      "supplier_id": 1,
      "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://warehouse:5000/api/v1/product", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_data = response_post.json()
    response_post = requests.request("PUT", f"http://warehouse:5000/api/v1/product/{response_data['id']}",
                                     headers=headers, data=payload)
    assert response_post.status_code == 200
    assert num_of_columns != len(response_data)
    assert not all([False for key in ["address", "id", "name", "create_at", "category_id", "problem"] if key not in response_data.keys()])
