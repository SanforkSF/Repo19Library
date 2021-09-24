from rest_framework import serializers
from .models import CustomUser
from .views import *

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email', 'password', 'updated_at',
                  'created_at', 'role', 'is_active']
