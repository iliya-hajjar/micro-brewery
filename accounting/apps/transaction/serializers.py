from rest_framework import serializers

from .models import Transaction, Payment


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['payment_type'] = PaymentSerializer(read_only=True)
        return super(TransactionSerializer, self).to_representation(instance)


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
