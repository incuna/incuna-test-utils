from django.db import models


class Stub(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
