from django.shortcuts import render
from rest_framework import viewsets
from main.models import Book, Journal
from main.serializers import BookSerializer, SimpleBookSerializer, JournalSerializer, SimpleJournalSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SimpleBookSerializer
        else:
            return BookSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

class JournalViewSet(viewsets.ModelViewSet):

    queryset = Journal.objects.all()
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return SimpleJournalSerializer
        else:
            return JournalSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)

        return [permission() for permission in permission_classes]

