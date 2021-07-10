from . import views
from django.urls import path, include
from rest_framework import routers
from .api.viewsets import BookViewSet, ClientReservesViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'client', ClientReservesViewSet)
#router.register(r'books/<int:pk>/reserve', RentedsBookViewSet)




urlpatterns = [
    path('', include(router.urls)),
    ]