from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response

from ..models import Book, RentBook, Client
from .serializers import BookSerializer, RentedsBookSerializer, ClientSerializer


class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['post'], detail=True, permission_classes=[IsAuthenticated],
            url_path='reserve', url_name='reserve')
    def reserve(self, request, pk=None):
        rent_book_dict = {}
        rent_book_dict['client_id'] = request.data.get('client')
        rent_book_dict['book_id'] = pk
        rent_book_dict['rented_at'] = request.data.get('rented_at')
        rent_book, created = RentBook.objects.get_or_create(**rent_book_dict)
        print(created)
        if created:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ClientReservesViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(methods=['get'], detail=True, permission_classes=[IsAuthenticated],
            url_path='books', url_name='books')
    def get_books(self, instance, pk=None):
        queryset = RentBook.objects.filter(client_id=pk)
        serializer = RentedsBookSerializer(queryset, many=True)
        return Response(serializer.data)