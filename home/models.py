from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class ItemType(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    image_url = models.TextField()
    type = models.ForeignKey(ItemType, blank=True, null=True, on_delete=models.SET_NULL)

