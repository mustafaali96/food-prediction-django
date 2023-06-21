from rest_framework import serializers
from revoke_app import models
from revoke_app.serializers import CategorySerializer

class IngredientNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = ('id', 'ingredient', 'quantity', 'get_unit_display', 'unit',)


class DishSerializer(serializers.ModelSerializer):
    country= serializers.CharField(source='country.country')
    category = CategorySerializer(many=True, read_only=True)
    foodCategory = serializers.CharField(source='foodCategory.foodCategory')
    Ingredient = IngredientNameSerializer(many=True, read_only=True)

    class Meta:
        model = models.Dish
        fields = ('id', 'name', 'foodQuantity', 'foodUnit', 'get_foodUnit_display', 'country', 'category', 'foodCategory', 'Ingredient',)

class PredictDishSerializer(serializers.ModelSerializer):
    country= serializers.CharField(source='country.country')
    category = CategorySerializer(many=True, read_only=True)
    foodCategory = serializers.CharField(source='foodCategory.foodCategory')
    Ingredient = IngredientNameSerializer(many=True, read_only=True)
    cusNote = serializers.SerializerMethodField('note')
    
    def note(self, foo):
        return foo.note.strip()

    class Meta:
        model = models.Dish
        fields = ('id', 'name', 'cusNote', 'foodQuantity', 'foodUnit', 'get_foodUnit_display', 'country', 'category', 'foodCategory', 'Ingredient',)