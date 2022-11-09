from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    image_url = models.TextField()

