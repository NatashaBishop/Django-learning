# ViewSets (shortcut)
# Combine logic for multiple actions (list, create, retrieve, etc.)

from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
