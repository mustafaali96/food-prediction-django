from rest_framework import serializers
from .models import UserProfile
from foodApp import models


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['email', 'name', 'gender', 'age', 'bp', 'sugar', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = UserProfile(email=self.validated_data['email'], name=self.validated_data['name'],
                            gender=self.validated_data['gender'], age=self.validated_data['age'],
                            bp=self.validated_data['bp'], sugar=self.validated_data['sugar'],)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={"input_type": "password"}, required=True)
    new_password = serializers.CharField(style={"input_type": "password"}, required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        return value
    
class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"

class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Dish
        fields = "__all__"

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingredient
        fields = "__all__"