from django.db import models

# Create your models here.


class Tafseer(models.Model):
    surah = models.IntegerField()
    ayah = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f"{self.surah}:{self.ayah}"
