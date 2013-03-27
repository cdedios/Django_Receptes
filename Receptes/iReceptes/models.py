from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
  name = models.CharField(max_length=40)
  description = models.TextField(max_length=1000)
  def __unicode__(self):
    return self.name

class Cuiner(models.Model):
  name = models.TextField(max_length=100)
  
class Recepta(models.Model):
  name = models.TextField(max_length=100)
  description = models.TextField(max_length=1000)
  ingredients = models.ForeingKey(Ingredtient)
  user = models.ForeingKey(User)
  def __unicode__(self):
    return self.ingredients.name+ " - "+self.description
