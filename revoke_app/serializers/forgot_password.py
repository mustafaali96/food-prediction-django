from rest_framework import serializers
from django.contrib.auth import get_user_model


class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)