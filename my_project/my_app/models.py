from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    location=models.CharField(max_length=50)

    class Meta:
        db_table="product"