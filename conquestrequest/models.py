from django.db import models

# Create your models here.
class Item(models.Model): 
    
    # name_of_cuisine = models.CharField(max_length=30)
    # id_for_dish = models.CharField(max_length=4)
    # price = models.IntegerField()
    # classification = models.CharField(max_length=10)
    # description = models.CharField(max_length=100)
    picture = models.FileField(upload_to='documents/')
    name = models.CharField(max_length=30, default='no description')
    description = models.CharField(max_length=100, default='no description')
    requestID = models.CharField(max_length=5, default='null')