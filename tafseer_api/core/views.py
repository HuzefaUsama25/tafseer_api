# views.py
from rest_framework import generics
from .models import Tafseer
from .serializers import TafseerSerializer

from rest_framework import filters


class TafseerListAPIView(generics.ListAPIView):
    queryset = Tafseer.objects.all()
    serializer_class = TafseerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text']
