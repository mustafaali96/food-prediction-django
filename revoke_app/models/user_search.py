from django.db import models

class UserSearch(models.Model):

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
    foodQuantity = models.IntegerField(null=False, blank=False)
    foodUnit = models.PositiveIntegerField(choices=UNIT_CHOICES, default=1, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    foodCategory = models.ForeignKey('FoodCategory', on_delete=models.CASCADE)
    Ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.created_at}"