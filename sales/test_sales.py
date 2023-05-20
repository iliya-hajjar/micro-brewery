"""
Because of the time limit did not finish test but the concept is clear we can do the following tests for all
other endpoints.
"""
import requests
import json


headers = {
  'Content-Type': 'application/json'
}


def test_order_details_pass():
    num_of_columns = 6
    data = {
        "user_id": 1,
        "product_count": 5,
        "product_id": 1,
        "order_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://host.docker.internal:8002/api/v1/order_detail", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://host.docker.internal:8002/api/v1/order_detail/{response_post.json()["order_details_id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns == len(response_data)
    assert all([False for key in response_data.keys() if key not in ["id", "product_count", "product_id", "order_id", "order", "created_at"]])


def test_order_details_fail():
    num_of_columns = 1
    data = {
        "user_id": 1,
        "product_count": 5,
        "product_id": 1,
        "order_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://host.docker.internal:8002/api/v1/order_detail", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://host.docker.internal:8002/api/v1/order_detail/{response_post.json()["order_details_id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns != len(response_data)
    assert not all([False for key in ["id", "product_count", "product_id", "order_id", "order", "created_at", "user_id"] if key not in response_data.keys()])