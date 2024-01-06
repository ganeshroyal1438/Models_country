from django.db import models

# Create your models here.

class Country(models.Model):
    Country_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Country_name

class Capitals(models.Model):
    Country_name=models.OneToOneField(Country,on_delete=models.CASCADE)
    Capital_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.Capital_name