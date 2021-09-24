from django.urls import path, include
from book.views import *
from author.views import *
from authentication.views import *
from order.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', AuthorViewSet)
router.register('book', BookViewSet)
router.register('user', CustomUserViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
