from . import views
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import BookViewSet, ClientReservesViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'client', ClientReservesViewSet, basename='client')




urlpatterns = [
    path('', include(router.urls)),
    ]