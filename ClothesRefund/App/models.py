from django.db import models

# This is the model for the clothes, it contains the name, the material, the size, the brand and the color of the clothes.

class Clothes(models.Model):
    ClothesName = models.CharField(max_length=200 , default='Enter a name')
    ClothesMaterial= models.CharField(max_length=200  ,default='Enter a material')
    ClothesSize = models.CharField(max_length=200 ,default='Enter a size')
    ClothesBrand = models.CharField(max_length=200 ,default='Enter a brand')
    ClothesColor= models.CharField(max_length=200 ,default='Enter a color')
    IDclothes = models.AutoField(primary_key=True,)
    def __str__(self):
        return self.name
