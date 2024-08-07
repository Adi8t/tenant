from django.db import models
from insta.models import Client
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.IntegerField() #harek ek hotel ne ek tenant associate karyu che.
    tenant = models.ForeignKey(Client,related_name='hotels', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
