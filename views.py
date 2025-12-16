
from rest_framework import generics
from .models import Book
from .serializers import Bookserializer 
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

