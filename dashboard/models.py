from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name