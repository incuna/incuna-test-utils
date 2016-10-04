from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'


class Relation(models.Model):
    pass


class ManyRelated(models.Model):
    relation = models.ManyToManyField(Relation)
