from rest_framework import serializers
from revoke_app import models

class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        # fields = "__all__"
        fields = ('id', 'name', 'foodQuantity', 'foodUnit', 'get_foodUnit_display', 'country', 'category', 'foodCategory', 'Ingredient',)