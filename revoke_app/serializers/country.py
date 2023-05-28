from rest_framework import serializers
from revoke_app import models

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = "__all__"