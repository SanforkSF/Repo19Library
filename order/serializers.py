from rest_framework import serializers
from .models import Order
from .views import *


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ['user', 'book', 'created_at', 'end_at', 'plated_end_at']
