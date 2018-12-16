from django.db import models
class Product(models.Model):
    productid = models.IntegerField()
    productname = models.CharField(max_length=30)
    productcost = models.IntegerField()
    productcolor = models.CharField(max_length=30)
    productweight = models.IntegerField()
