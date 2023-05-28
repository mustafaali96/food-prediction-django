from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

import base64
import uuid
import six
import imghdr


class Base64ImageField(serializers.ImageField):
    """
        A django-rest-framework field for handling image-uploads through raw post data.
        It uses base64 for en-/decoding the contents of the file.
        """

    def to_internal_value(self, data):
        # Check if this is a base64 string
        if not data:
            return None

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)


    def get_file_extension(self, filename, decoded_file):
        extension = imghdr.what(filename, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension


class RegisterUserSerializer(serializers.ModelSerializer):

    profile_picture = Base64ImageField(required=False)
    password2 = serializers.CharField(
        label=_("Password confirmation"),
        help_text=_("Enter the same password as before, for verification."),
        write_only= True
    )

    class Meta:
        model = get_user_model()
        fields = ("id", "full_name", "age", "gender", "bp", "sugar", "phone_number", "email", "profile_picture", "password", "password2")
        # read_only_fields = ("id", "full_name", "age", "gender", "bp", "sugar", "phone_number", "email")
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "id": {
                "read_only": True
            },
        }
    
    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.get('password', None)
        password2 = validated_data.pop('password2', "")
        if password != password2:
            raise serializers.ValidationError({"password": 'Passwords do not match.'})

        return self.Meta.model.objects.create_user(email, **validated_data)
    
    def update(self, instance, validated_data):
        
        validated_data.pop("password", None)
        validated_data.pop('password2', None)
        
        return super().update(instance, validated_data)
        