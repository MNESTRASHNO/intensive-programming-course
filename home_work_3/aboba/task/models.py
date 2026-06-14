from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=128)
    privileges = models.CharField(max_length=6)
    description = models.TextField(blank=True)
