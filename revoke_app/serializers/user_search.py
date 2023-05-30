from rest_framework import serializers
from revoke_app import models

class UserSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserSearch
        fields = "__all__"
