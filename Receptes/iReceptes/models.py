from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


### CATEGORIA 
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=120, unique=True)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)
    
    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('categoria_detail',kwargs={'idArquitecte':self.pk})

### ALIMENT
class Aliment(models.Model):
    idAliment = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=150)
    group = models.CharField(max_length=40)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('detail_aliment',kwargs={'idAliment':self.pk})

### METODEPREPARACIO
class MetodePreparacio(models.Model):
    idMetode = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=60, blank=True)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.nom

    def get_absolute_url(self):
      return reverse('detail_metode',kwargs={'idMetode':self.pk})

### RECEPTA
class Recepta(models.Model):
  idRecepta  = models.AutoField(primary_key=True)
  nom = models.CharField(max_length=40)
  description = models.TextField(max_length=400, blank=True)
  category = models.ForeignKey(Categoria)
  user = models.ForeignKey(User)
  date = models.DateField(default=date.today)

  def __unicode__(self):
    return self.nom

    def get_absolute_url(self):
      return reverse('detail_recepta',kwargs={'idRecepta':self.pk})

### PAS
class Pas(models.Model):
    idPas = models.AutoField(primary_key=True)
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
      return reverse('detail_pas',kwargs={'idPas':self.pk})

### INGREDIENT
class Ingredient(models.Model):
  idIngredient = models.AutoField(primary_key=True)
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
      return reverse('detail_ingredient',kwargs={'id':self.id})

