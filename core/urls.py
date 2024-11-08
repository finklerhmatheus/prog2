
from django.urls import path
from .views import index, contato, pedido, produto

urlpatterns = [
    path('', index),
    path('contato',contato),
    path('pedido',pedido),
    path('produto/<int:pk>', produto, name='produto')
]

