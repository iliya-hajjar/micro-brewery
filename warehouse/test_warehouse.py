"""
Because of the time limit did not finish test but the concept is clear we can do the following tests for all
other endpoints.
"""
import requests
import json


headers = {
  'Content-Type': 'application/json'
}


def test_supplier_pass():
    num_of_columns = 5
    data = {
        "name": "amazon",
        "address": "sssssssssssssssss",
        "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://host.docker.internal:8001/api/v1/supplier", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://host.docker.internal:8001/api/v1/supplier/{response_post.json()["id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns == len(response_data)
    assert all([False for key in response_data.keys() if key not in ["address", "id", "name", "create_at", "category_id"]])


def test_supplier_fail():
    num_of_columns = 6
    data = {
        "name": "amazon",
        "address": "sssssssssssssssss",
        "category_id": 1
    }
    payload = json.dumps(data)
    response_post = requests.request("POST", "http://host.docker.internal:8001/api/v1/supplier", headers=headers, data=payload)
    assert response_post.status_code == 200

    response_get = requests.get(f'http://host.docker.internal:8001/api/v1/supplier/{response_post.json()["id"]}')
    assert response_get.status_code == 200
    response_data = response_get.json()
    assert num_of_columns != len(response_data)
    assert not all([False for key in ["address", "id", "name", "create_at", "category_id", "problem"] if key not in response_data.keys()])