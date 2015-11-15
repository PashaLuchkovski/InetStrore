from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    imagePath = models.CharField()


class User(models.Model):
    login = models.CharField(null=True)
    password = models.CharField(null=True)
    phoneNumber = models.CharField(max_length=15, null=True)
    vkId = models.CharField()
    basket = models.ManyToManyField(Product)
