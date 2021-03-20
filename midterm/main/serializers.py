from rest_framework import serializers
from main.models import Book, Journal
from drf_writable_nested.serializers import WritableNestedModelSerializer

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        field = '__all__'

class SimpleBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'price', 'genre')

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'

class SimpleJournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('name', 'price', 'type')