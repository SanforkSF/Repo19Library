from django.urls import path
from .views import *

urlpatterns = [
    path('', BookListAPIView.as_view(), name='api_book'),
]
