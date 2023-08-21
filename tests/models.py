from django.db import models
from django.contrib.auth.models import User

from dashboard.models import Room
import string, random

# Create your models here.
def add_ellipses(text):
    if len(text) > 50:
        return text[:50] + ...
    else:
        return text

def generate_code():
    length = 6
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Test.objects.filter(code=code).count() == 0:
            break
    return code

class Test(models.Model):
    TestType = models.TextChoices('TestType', 'QUIZ EXAM')
    title = models.CharField(max_length=250)
    type = models.CharField(blank=False, choices=TestType.choices, max_length=10)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=8, default=generate_code, unique=True, null=False)
    expiration = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        add_ellipses(self.title)