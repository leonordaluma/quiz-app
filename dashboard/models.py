from django.db import models
from django.contrib.auth.models import User

def add_ellipses(text):
    if len(text) > 50:
        return text[:50] + ...
    else:
        return text

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Test(models.Model):
    TestType = models.TextChoices('TestType', 'QUIZ EXAM')
    title = models.CharField(max_length=250)
    type = models.CharField(blank=False, choices=TestType.choices, max_length=10)
    description = models.TextField(blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        add_ellipses(self.title)

