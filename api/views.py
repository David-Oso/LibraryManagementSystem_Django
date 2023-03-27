from django.shortcuts import render
from rest_framework import generics

from api.serializers import BookSerializer
from book.models import Book


# Create your views here.


class BookCreateApiView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
