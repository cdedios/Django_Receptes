Django_Receptes
===============
##What is Django?
Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

##Recipe Book
Introduction:
This is a web-app that implements a Recipe book. I've used 8 models to represent the app.

Ingredient:
quantitat / quantitiy: (floatField)
unitat / unit: charField
recepta / recipe: foreingKey(Recepta)
aliment: foreingKey(Aliment)
prep_method: foreingKey(MetodePreparacio)
pas / step: foreingKey(Pas)
calories = models.FloatField() 
carbohydrateContent = models.FloatField()
user = models.ForeignKey(User) 
date = models.DateField(default=date.today)
Pas / Step:
text: (textField )
recepta: foreingKey(Recepta)
ordre (integerField)
user = models.ForeignKey(User) 
date = models.DateField(default=date.today)
Recepta / Recipe :
nom: (charField max = 40)
description: (textField max = 400)
category : foreingKey(Categoria)
user = models.ForeignKey(User) 
date = models.DateField(default=date.today)
pais: models.CharField(max_length=40)
Categoria / Cathegory:
nom (charField max = 120)
user = models.ForeignKey(User) 
date = models.DateField(default=date.today)
Aliment:
nom_aliment: (charField max =150)
group: (charField max = 40)
user = models.ForeignKey(User) 
date = models.DateField(default=date.today)
MetodePreparacio / PreparationMode:
nom: (charField max = 60)
user = models.ForeignKey(User) 
date = models.DateField(default=date.today)



En aquesta nova entrega he afegit la classe opino (Review) per a poder opinar sobre les diferents receptes.
Review: 
 RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')) 
 rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES) 
comment = models.TextField(blank=True, null=True) 
user = models.ForeignKey(User,blank=False) 
date = models.DateField(default=date.today) 
ReceptaReview / RecipeReview:
recepta = models.ForeignKey(Recepta) 
	
Consideracions rellevants:
La base de dades te com a usuari i pasword carlos.
En aquesta part he afegit el marcat semàntic basat en RDFa en les pagines de Recepta.html i de Ingredient.html. Les propietats que he fet servir les he tret de schema.org i són les següents:

Recipe :
name
description
recipeCuisine
recipeInstructions
ingredients
recipeCategory

Ingredient
calories
carbohidrates

En aquesta imatge podem veure perfectament com s'estructuren els següents elements.



