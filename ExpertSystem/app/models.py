from django.db import models

# Create your models here.

class fact(models.Model):
    fact_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    discription = models.CharField(max_length=300)
    
    def __str__(self): 
      return type

class solution(models.Model):
    sol_id = models.AutoField(primary_key=True)
    fact_id= models.ForeignKey(fact, on_delete=models.CASCADE) 
    type = models.CharField(max_length=255)
    discription = models.CharField(max_length=300)
    
    def __str__(self): 
      return type