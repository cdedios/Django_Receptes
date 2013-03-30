from django.db import models
from django.contrib.auth.models import User

# Create your models here.

### UNITAT
class Unitat(models.Model):
    nom = models.CharField(max_length=60)
#    name_abbrev = models.CharField(max_length=60, blank=True)
#    plural = models.CharField(max_length=60, blank=True)
#    plural_abbrev = models.CharField(max_length=60, blank=True)
    type = models.IntegerField(choices=((0, 'Altres'),(1, 'Massa'),(2, 'Volum')))

    def __unicode__(self):
        return self.plural

    class Meta:
        ordering = ["nom"]
###GRUP ALIMENTARI (peix, carn, pasta, arros, amanides...)
class GrupAlimentari(models.Model):
    nom = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ["nom"]

### CATEGORIA (base, diari, de tan en quan..)
class Categoria(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    #parent = models.ForeignKey('self', null=True, blank=True, related_name='child_set')
    order_index = models.PositiveIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.nom

    class Meta:
        #verbose_name_plural = 'Categories'
        ordering = ["order_index"]

### ALIMENT
class Aliment(models.Model):
    nom = models.CharField(max_length=150)
    group = models.ForeignKey(GrupAlimentari)

    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ["nom", "group"]

### METODEPREPARACIO
class MetodePreparacio(models.Model):
    nom = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.nom

    def save(self):
        self.nom = self.nom.lower()
        super(MetodePreparacio, self).save()

### RECEPTA
class Recepta(models.Model):
  nom = models.CharField(max_length=40)
  description = models.TextField(max_length=400, blank=True)

#  sources = models.ManyToManyField(Source, blank=True)
  category = models.ForeignKey(Categoria)
  #tags = TagField()

  #user = models.ForeignKey(User)
  def __unicode__(self):
    return self.nom
  class Meta:
    ordering = ['nom']

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

    class Meta:
        ordering = ['order', 'id']




### INGREDIENT
class Ingredient(models.Model):

  quantitat = models.FloatField()#core=True)
  #amountMax = models.FloatField(null=True, blank=True)
  unitat = models.ForeignKey(Unitat,null=True, blank=True)
  recepta = models.ForeignKey(Recepta)
  aliment = models.ForeignKey(Aliment)
  prep_method = models.ForeignKey(MetodePreparacio, null=True,blank=True)
  order_index = models.PositiveIntegerField(blank=True, null=True)
  pas = models.ForeignKey(Pas, blank=True, null=True)


  #def __init__(self, *args, **kwargs):
   #   super(Ingredient, self).__init__(*args, **kwargs)

 # def choices_for__pas(self):
 #     return Pas.objects.filter(recepta=self.recepta_id)

  def __unicode__(self):
      quantitat = str(int(self.quantitat) if self.quantitat == int(self.quantitat) else self.quantitat)
      unitat = str((self.unitat.nom if self.unitat != None else '') if self.quantitat
              == 1 and self.amountMax is None else (self.unitat.plural if
                  self.unitat != None else ''))
      aliment = str(self.aliment).lower()
      return "%s %s %s" % (quantitat, unitat, aliment)

  class Meta:
      ordering = ["pas", "order_index", "id"]

