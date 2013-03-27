from django.db import models

# Create your models here.

class Ingredient(models.Model):
  name = models.TextField(max_length=100)
  description = models.TextField(max_length=1000)

class Cuiner(models.Model):
  name = models.TextField(max_length=100)
  
class Recepta(models.Model):
  name = models.TextField(max_length=100)
