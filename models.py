from django.db import models

# Create your models here.

# inheriting the model from the model class

class foodItems(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    