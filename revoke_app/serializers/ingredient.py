from rest_framework import serializers
from revoke_app import models

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        # fields = "__all__"
        exclude = ('quantity', 'unit', )