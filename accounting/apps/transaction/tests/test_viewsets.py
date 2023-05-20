import json

import requests
from django.test import TestCase

headers = {
  'Content-Type': 'application/json'
}


class TransactionViewSetTest(TestCase):

    def test_transaction_create(self):
        url_tx = "http://localhost:8000/api/v1/transaction/transactions"

        payload_tx = json.dumps({
            "order_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "amount": 0,
            "description": "string",
            "is_confirmed": True,
            "payment_type": 1
        })
        response = requests.request("POST", url_tx, headers=headers, data=payload_tx)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertTrue(data['is_confirmed'])
        self.assertEqual(data['description'], "string")
        self.assertEqual(data['order_id'], "3fa85f64-5717-4562-b3fc-2c963f66afa6")
        self.assertEqual(data['amount'], 0)

    def test_payment_create(self):
        url_payment = "http://localhost:8000/api/v1/transaction/payments"
        payload_payment = json.dumps({
            "type": "CRYPTO"
        })
        response = requests.request("POST", url_payment, headers=headers, data=payload_payment)
        self.assertEqual(response.status_code, 201)
