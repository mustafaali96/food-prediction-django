from rest_framework import serializers
from revoke_app import models

class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FoodCategory
        fields = "__all__"