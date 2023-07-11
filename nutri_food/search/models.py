
from django.db import models


class Product(models.Model):
    ingredients = models.CharField(max_length=2000000,null=True)
    nutri_score = models.CharField(max_length=2000000,null=True)
    name = models.CharField(max_length=250000,null=True)
    brand = models.CharField(max_length=250000,null=True)
    category = models.CharField(max_length=250000,null=True)
    
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    alternatives  = models.ManyToManyField('ProductPair')


class ProductPair(models.Model):
    user_rec = models.ForeignKey(User, on_delete=models.CASCADE)
    first_product = models.CharField(max_length=200)
    alternative_product = models.CharField(max_length=200)

    # first_product = models.ManyToManyField('Product')
    # alternative_product = models.ManyToManyField('Product')




# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)