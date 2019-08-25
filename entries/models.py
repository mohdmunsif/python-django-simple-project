from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Entries(models.Model):
    toyname = models.CharField(max_length=100)
    descr = models.TextField()
    url = models.URLField(max_length=400)
    age_lower = models.IntegerField()
    age_upper = models.CharField(max_length=300)
    image_path = models.CharField(max_length=300)
    image_upload = models.FileField(upload_to='images/', blank=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="entryusername")
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.toyname} {self.descr}"
