from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100,blank=True, null=True)
    title=models.CharField(max_length=500,blank=True, null=True)
    description=models.CharField(max_length=500,blank=True, null=True)
    published=models.DateTimeField(blank=True, null=True)
    urlToImage=models.CharField(max_length=400,blank=True, null=True)


