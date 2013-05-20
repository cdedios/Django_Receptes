from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


### CATEGORIA (base, diari, de tan en quan..)
class Categoria(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    
    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('detail_categoria',kwargs={'id':self.pk})

### ALIMENT
class Aliment(models.Model):
    nom = models.CharField(max_length=150)
    group = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('detail_aliment',kwargs={'idAliment':self.pk})

### METODEPREPARACIO
class MetodePreparacio(models.Model):
    nom = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('detail_metode',kwargs={'idMetode':self.pk})

### RECEPTA
class Recepta(models.Model):
  nom = models.CharField(max_length=40)
  description = models.TextField(max_length=400, blank=True)
  category = models.ForeignKey(Categoria)

  def __unicode__(self):
    return self.nom

    def get_absolute_url(self):
      return reverse('detail_recepta',kwargs={'idRecepta':self.pk})

### PAS
class Pas(models.Model):
    
    text = models.TextField(blank=True)
    recepta = models.ForeignKey(Recepta)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        ret = self.text[:40]
        if len(self.text) > 40:
            ret += "..."
        return ret

    def get_absolute_url(self):
      return reverse('detail_pas',kwargs={'idPas':self.pk})

### INGREDIENT
class Ingredient(models.Model):

  quantitat = models.FloatField()
  unitat = models.CharField(max_length=40)
  recepta = models.ForeignKey(Recepta,blank=True, null=True)
  aliment = models.ForeignKey(Aliment,blank=True, null=True)
  prep_method = models.ForeignKey(MetodePreparacio, null=True,blank=True)
  pas = models.ForeignKey(Pas, blank=True, null=True)


  def __unicode__(self):      
      return u' %f %s %s '%(self.quantitat,self.unitat,self.aliment.nom)

  def get_absolute_url(self):
      return reverse('detail_ingredient',kwargs={'id':self.id})

