from rest_framework import serializers
from revoke_app import models

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"