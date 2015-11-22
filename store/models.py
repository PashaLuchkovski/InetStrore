from django.db import models

# Create your models here.

ADMIN = 'ADMIN'
USER = 'USER'
CHECKER = 'CHECKER'

# class Product(models.Model):
#     name = models.CharField(max_length=150)
#     description = models.TextField()
#     price = models.IntegerField()
#     count = models.IntegerField()
#     imagePath = models.CharField()


class User(models.Model):
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    login = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20,null=True)
    phoneNumber = models.CharField(max_length=15, null=True)
    vkId = models.CharField(max_length=15,null=True)
    permissions = models.CharField(max_length=20, default=USER)
    # basket = models.ManyToManyField(Product, null=True)
