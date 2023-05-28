import uuid
from django.db import models


class CreatedAtField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAtField(models.Model):
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def generate_uuid():
    return uuid.uuid4().hex


class ModelUUIDField(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=generate_uuid, editable=False)

    class Meta:
        abstract = True


class CreatedAndUpdatedModelFields(CreatedAtField, UpdatedAtField):
    
    class Meta:
        abstract = True