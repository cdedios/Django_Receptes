from django.db import models
from django.contrib.auth.models import User


### CATEGORIA (base, diari, de tan en quan..)
class Categoria(models.Model):
    nom = models.CharField(max_length=120, unique=True)

    def __unicode__(self):
        return self.nom

### ALIMENT
class Aliment(models.Model):
    nom = models.CharField(max_length=150)
    group = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nom

### METODEPREPARACIO
class MetodePreparacio(models.Model):
    nom = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.nom

### RECEPTA
class Recepta(models.Model):
  nom = models.CharField(max_length=40)
  description = models.TextField(max_length=400, blank=True)
  category = models.ForeignKey(Categoria)

  def __unicode__(self):
    return self.nom

### PAS
class Pas(models.Model):
    
    text = models.TextField(blank=True)#, core=True)
    recepta = models.ForeignKey(Recepta)
    order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        ret = self.text[:40]
        if len(self.text) > 40:
            ret += "..."
        return ret

### INGREDIENT
class Ingredient(models.Model):

  quantitat = models.FloatField()#core=True)
  unitat = models.CharField(max_length=40)
  recepta = models.ForeignKey(Recepta,blank=True, null=True)
  aliment = models.ForeignKey(Aliment,blank=True, null=True)
  prep_method = models.ForeignKey(MetodePreparacio, null=True,blank=True)
  pas = models.ForeignKey(Pas, blank=True, null=True)


  def __unicode__(self):      
      return u'asdfas %f %s %s '%(self.quantitat,self.unitat,self.aliment.nom)

