from django.db import models

# Create your models here.
class Search(models.Model) :
    stock= models.CharField(max_length=100)
    ordertype = models.CharField(max_length=10)
    price = models.FloatField()
    quantity = models.IntegerField()




class adm(models.Model):
    sno= models.IntegerField()
    sname= models.CharField(max_length=100)
    orderq= models.IntegerField()
    ordert= models.CharField(max_length=100)
    executeq= models.CharField(max_length=100)
    pri = models.DoubleField()
    order_sta= models.CharField()
    order_date= models.DateTime.Field(auto_now= True)

