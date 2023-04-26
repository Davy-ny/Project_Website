from django.db import models


class Tree(models.Model):
    species = models.CharField(max_length=30, blank=False, null=False)
    handler = models.CharField(max_length=30, blank=False, null=False)
    number = models.IntegerField(blank=False, null=False)
    date = models.CharField(max_length=30, blank=False, null=False)


def __str__(self):
    self.name
