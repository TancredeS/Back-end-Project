from django.db import models

# This is the model for the clothes, it contains the name, the material, the size, the brand and the color of the clothes.

class Clothes(models.Model):
    ClothesName = models.CharField(max_length=200 , default='ENTER A NAME')
    ClothesMaterial= models.CharField(max_length=200  ,default='ENTER A MATERIAL')
    ClothesSize = models.CharField(max_length=200 ,default='ENTER A SIZE')
    ClothesBrand = models.CharField(max_length=200 ,default='ENTER A BRAND')
    ClothesColor= models.CharField(max_length=200 ,default='ENTER A COLOR')
    IDclothes = models.AutoField(primary_key=True,)
    def __str__(self):
        return self.name
