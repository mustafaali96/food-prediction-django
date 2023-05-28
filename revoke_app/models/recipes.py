from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category
    
class FoodCategory(models.Model):
    foodCategory = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.foodCategory
    
class Ingredient(models.Model):

    # unit choices
    KG = 1
    TS = 2
    TBS = 3
    CUP = 4
    POUND = 5
    LITTER = 6
    GRAMS = 7
    AMT = 8
    OUNCE = 9
    UNIT_CHOICES = (
        (KG, "Kilogram"),
        (TS, "Tea Spoon"),
        (TBS, "Table Spoon"),
        (CUP, "Cup"),
        (POUND, "Pound"),
        (LITTER, "Litter"),
        (GRAMS, "Grams"),
        (AMT, ""),
        (OUNCE, "Ounce"),
    )

    ingredient = models.CharField(max_length=50, unique=False)
    quantity = models.FloatField(null=False, blank=False)
    unit = models.PositiveIntegerField(choices=UNIT_CHOICES, default=1, null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.ingredient}" 
    
class Dish(models.Model):

    # unit choices
    KG = 1
    POUND = 2
    LITTER = 3
    AMT = 4
    UNIT_CHOICES = (
        (KG, "Kilogram"),
        (POUND, "Pound"),
        (LITTER, "Litter"),
        (AMT, ""),
    )
    name = models.CharField(max_length=50, unique=True)
    foodQuantity = models.IntegerField(null=True, blank=True)
    foodUnit = models.PositiveIntegerField(choices=UNIT_CHOICES, default=1, null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    foodCategory = models.ForeignKey('FoodCategory', on_delete=models.CASCADE)
    Ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.foodQuantity} {self.foodUnit} {self.name}" 