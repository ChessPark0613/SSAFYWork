from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField("상품명", max_length=100)
    discription = models.TextField("상품설명")
    price = models.IntegerField("가격")
    is_published = models.BooleanField("")