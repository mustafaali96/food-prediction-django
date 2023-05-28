from rest_framework import serializers


class PredictFoodSerializer(serializers.Serializer):

    country = serializers.CharField(max_length=25, required=True)
    category = serializers.CharField(max_length=25, required=True)
    food_category = serializers.CharField(max_length=100, required=True)
    food_name = serializers.CharField(max_length=50, required=True)
    other = serializers.CharField(max_length=100, required=False, allow_null=True)

