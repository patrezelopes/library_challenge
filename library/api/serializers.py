from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import Book, RentBook, Client


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class RentedsBookSerializer(serializers.HyperlinkedModelSerializer):
    client = SerializerMethodField()
    book = SerializerMethodField()
    finerate = SerializerMethodField()

    def get_client(self, instance):
        return instance.client.name

    def get_book(self, instance):
        return instance.book.name

    def get_finerate(self, instance):
        return str(instance.finerate())

    class Meta:
        model = RentBook
        fields = ['client', 'book', 'rented_at', 'finerate']