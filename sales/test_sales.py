import requests
import json
import requests_mock

headers = {
  'Content-Type': 'application/json'
}


def send_data(payload):
    response = requests.request("POST", "http://sales:5000/api/v1/order_detail", headers=headers, data=payload)
    return response.json()


def get_data(id):
    response = requests.get(f'http://sales:5000/api/v1/order_detail/{id}')
    return response


def test_order_details_pass(requests_mock):
    num_of_columns = 5
    data = {
        "amount": 5000,
        "user_id": 1,
        "product_count": 1,
        "product_id": 1,
        "payment_id": 1
    }
    payload = json.dumps(data)
    mocked_response = {"status": 200, "order_details_id": 1}
    requests_mock.post('http://sales:5000/api/v1/order_detail', json=mocked_response)
    response = send_data(payload)

    mocked_response = {
        'id': 1,
        'order_id': mocked_response['order_details_id'],
        'product_id': 1,
        'product_count': 'value',
        'created_at': 'value',
    }
    requests_mock.get(f'http://sales:5000/api/v1/order_detail/{response["order_details_id"]}', json=mocked_response)
    assert get_data(response["order_details_id"]).status_code == 200
    assert num_of_columns == len(get_data(response["order_details_id"]).json())
    assert all([False for key in get_data(response["order_details_id"]).json().keys() if key not in
                ["id", "product_count", "product_id", "order_id", "order", "created_at"]])


def test_order_details_fail(requests_mock):
    num_of_columns = 2
    data = {
        "amount": 5000,
        "user_id": 1,
        "product_count": 1,
        "product_id": 1,
        "payment_id": 1
    }
    payload = json.dumps(data)
    mocked_response = {"status": 200, "order_details_id": 1}
    requests_mock.post('http://sales:5000/api/v1/order_detail', json=mocked_response)
    response = send_data(payload)

    mocked_response = {
        'order_id': mocked_response['order_details_id'],
        'product_id': 1,
        'product_count': 'value',
        'created_at': 'value',
    }
    requests_mock.get(f'http://sales:5000/api/v1/order_detail/{response["order_details_id"]}', json=mocked_response)
    assert get_data(response["order_details_id"]).status_code == 200
    assert num_of_columns != len(get_data(response["order_details_id"]).json())
    assert not all([False for key in ["id", "product_count", "product_id", "order_id", "order", "created_at"] if key not
                    in get_data(response["order_details_id"]).json().keys()])
