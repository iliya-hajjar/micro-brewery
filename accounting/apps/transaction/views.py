import requests
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Transaction, Payment
from .serializers import TransactionSerializer, PaymentSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

    def list(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Transaction.objects.get(id=pk)
        serializer = TransactionSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        transaction = Transaction.objects.get(id=pk)
        serializer = TransactionSerializer(instance=transaction, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if transaction.is_confirmed:
            payload = {"transaction_id": transaction.id}
            requests.request("PUT", f"http://sales:5000/api/v1/order/{transaction.order_id}",
                             headers={'Content-Type': 'application/json'}, data=payload)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        transaction = Transaction.objects.get(id=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def list(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Payment.objects.get(id=pk)
        serializer = PaymentSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        transaction = Payment.objects.get(id=pk)
        serializer = PaymentSerializer(instance=transaction, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        transaction = Payment.objects.get(id=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
