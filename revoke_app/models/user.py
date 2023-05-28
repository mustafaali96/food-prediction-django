from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator, MinLengthValidator

from revoke_app.models.others import *
from .enums import GenederEnums, BPEnums, SugarEnums


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email is a required field.")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **kwargs):
        superuser = self.create_user(email, password, **kwargs)
        superuser.is_staff = True
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class User(ModelUUIDField, CreatedAndUpdatedModelFields, AbstractBaseUser, PermissionsMixin):
    
    full_name = models.CharField(
        max_length=50, 
        validators=[
            MinLengthValidator(3)
        ]
    )
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=GenederEnums.choices, blank=False, null=False)
    bp = models.CharField(max_length=50, choices=BPEnums.choices, blank=False, null=False)
    sugar = models.CharField(max_length=50, choices=SugarEnums.choices, blank=False, null=False)
    phone_number = models.CharField( 
        max_length=13,
        validators=[
            MinLengthValidator(11),
            RegexValidator(
                regex=r"^(?=.{11,13})\d+$",
                message="Given value doesn't meet the pattern requirements"
            )
        ]
    )
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ("full_name", "age", "gender", "bp", "sugar", "phone_number")

    objects = UserManager()

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        ordering = ("-created_at",)
    

