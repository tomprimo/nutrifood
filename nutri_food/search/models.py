
from django.db import models


class Produit(models.Model):
    ingredients = models.CharField(max_length=200)
    


