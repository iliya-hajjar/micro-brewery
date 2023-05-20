from django.urls import path

from .views import TransactionViewSet, PaymentViewSet

urlpatterns = [
    path('transactions', TransactionViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('transactions/<str:pk>', TransactionViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('payments', PaymentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('payments/<str:pk>', PaymentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
