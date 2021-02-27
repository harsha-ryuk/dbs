from django.db import models

# Create your models here.
class Search(models.Model) :
    stock= models.CharField(max_length=100)
    ordertype = models.CharField(max_length=10)
    price = models.FloatField()
    quantity = models.IntegerField()


class

