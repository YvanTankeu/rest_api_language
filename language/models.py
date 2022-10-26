from email.policy import default
from random import choices
from django.db import models

class Language(models.Model):
    Type_language = [  
        ('HN', 'Haut niveau'),
        ('LA', 'Assembleur'),
        ('LMe', 'Machine'),
        ('LMl', 'Materiel'),
    ] 
    RATING_STARS = [
        ('1', '1 etoile'),
        ('2', '2 etoiles'),
        ('3', '3 etoiles'),
        ('4', '4 etoiles'),
        ('4', '5 etoiles'),
    ]  
    name = models.CharField(max_length = 15)
    release_date = models.IntegerField()
    description = models.TextField() 
    type = models.CharField(
        max_length = 5, 
        choices = Type_language,
    )
    poo = models.BooleanField(default = False)
    rating = models.CharField(
        max_length = 1, 
        choices = RATING_STARS,
    )
    def __str__(self):
        return f'{self.name}'
    
class Framework(models.Model):
    name = models.CharField(max_length = 15)
    release_date = models.IntegerField()
    description = models.TextField() 
    rating = models.CharField(max_length = 1, choices = Language.RATING_STARS)
    language = models.ForeignKey('Language', on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.name}'
