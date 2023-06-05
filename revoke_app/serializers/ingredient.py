from rest_framework import serializers
from revoke_app import models

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ('id', 'ingredient',)
        # fields = ('id', 'ingredient', 'quantity', 'get_unit_display', 'unit',)