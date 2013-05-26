from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


### CATEGORIA 
class Categoria(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)
    
    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('categoria_detail',kwargs={'id':self.pk})

### ALIMENT
class Aliment(models.Model):
    nom_aliment = models.CharField(max_length=150)
    group = models.CharField(max_length=40)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.nom_aliment

    def get_absolute_url(self):
      return reverse('aliment_detail',kwargs={'id':self.pk})

### METODEPREPARACIO
class MetodePreparacio(models.Model):
    nom = models.CharField(max_length=60, blank=True)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('metode_detail',kwargs={'id':self.pk})

### RECEPTA
class Recepta(models.Model):
  nom = models.CharField(max_length=40)
  description = models.TextField(max_length=400, blank=True)
  category = models.ForeignKey(Categoria)
  pais = models.CharField(max_length=40)
  user = models.ForeignKey(User)
  date = models.DateField(default=date.today)
 

  def __unicode__(self):
    return self.nom

    def get_absolute_url(self):
      return reverse('recepta_detail',kwargs={'id':self.pk})

### PAS
class Pas(models.Model):
    text = models.TextField(blank=True)
    recepta = models.ForeignKey(Recepta)
    order = models.IntegerField(blank=False, null=True)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        ret = self.text[:40]
        if len(self.text) > 40:
            ret += "..."
        return ret

    def get_absolute_url(self):
      return reverse('pas_detail',kwargs={'id':self.pk})

### INGREDIENT
class Ingredient(models.Model):
  quantitat = models.FloatField()
  unitat = models.CharField(max_length=40)
  recepta = models.ForeignKey(Recepta,blank=True, null=True)
  aliment = models.ForeignKey(Aliment,blank=True, null=True)
  prep_method = models.ForeignKey(MetodePreparacio, null=True,blank=True)
  pas = models.ForeignKey(Pas, blank=True, null=True)
  user = models.ForeignKey(User)
  date = models.DateField(default=date.today)


  def __unicode__(self):      
      return u' %f %s %s '%(self.quantitat,self.unitat,self.aliment.nom)

  def get_absolute_url(self):
      return reverse('ingredient_detail',kwargs={'id':self.id})

