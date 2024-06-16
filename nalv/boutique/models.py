from django.db import models

"""
- Une marque
_ Une serie
- Une categorire
_ Le type de moteur
- Le numero d'immatriculation
_ Une description
- Un prix
- Une couleur
- Un slug
- Une image
"""


# Create your models here.
class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)
    moteur = models.CharField(max_length=100)
    immatriculation = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=290, blank=True)
    couleur = models.CharField(max_length=100)
    prix = models.IntegerField()
    slug = models.SlugField()
    image = models.ImageField(upload_to='images_des_voitures', blank=True, null=True)

    def __str__(self):
        return self.marque
