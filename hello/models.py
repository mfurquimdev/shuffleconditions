from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Condition(models.Model):
    number = models.IntegerField()
    shuffled = models.CharField(max_length=25)
