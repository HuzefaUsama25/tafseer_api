from .views import TafseerListAPIView
from django.urls import path

urlpatterns = [
    path('tafseer/', TafseerListAPIView.as_view(), name='tafseer-list'),
]
