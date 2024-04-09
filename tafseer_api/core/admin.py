from django.contrib import admin
from .models import Tafseer  # Import your model


@admin.register(Tafseer)
class TafseerAdmin(admin.ModelAdmin):
    search_fields = ['text']
