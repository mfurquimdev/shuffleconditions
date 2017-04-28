from django.db import models

# Create your models here.
class NumberIndex(models.Model):
    seqlength = models.IntegerField()
    index = models.IntegerField()
    sequence = models.CharField(max_length=50)
