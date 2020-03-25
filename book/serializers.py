from rest_framework.serializers import ModelSerializer
from .models import Book
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']
