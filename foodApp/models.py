from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.
# class UserProfile(AbstractBaseUser):

#     # user gender
#     MALE = 1
#     FEMALE = 2
#     GENDER_CHOICES = (
#         (MALE, "Male"),
#         (FEMALE, "Female"),
#     )

#     name = models.CharField(max_length=255, null=False, blank=False)
#     username = models.CharField(max_length=64, null=False, blank=False, unique=True)
#     email = models.EmailField(null=False, blank=False, unique=True)
#     age = models.PositiveIntegerField(null=False, blank=False)
#     gender = models.PositiveIntegerField(choices=GENDER_CHOICES, default=1)
#     contact = models.CharField(max_length=15, null=True, blank=True)
#     bp = models.IntegerField(null=False, blank=False)
#     sugar = models.IntegerField(null=False, blank=False)
#     # is_superuser = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'

#     REQUIRED_FIELDS = ['name', 'username', 'gender', 'age', 'bp', 'sugar']

#     def __str__(self):
#         return f"{self.name} | {self.email}" 

#     def is_male(self):
#         return self.gender == 1
    
#     def is_female(self):
#         return self.gender == 2
    



import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone



DISCOUNT_CODE_TYPES_CHOICES = [
    ('percent', 'Percentage-based'),
    ('value', 'Value-based'),
]


# Create your models here
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, gender, age, bp, sugar, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            gender=gender,
            age=age,
            bp=bp,
            sugar=sugar,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender, age, bp, sugar, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            gender=gender,
            age=age,
            bp=bp,
            sugar=sugar,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):

    # user gender
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    gender = models.PositiveIntegerField(choices=GENDER_CHOICES, default=1)
    contact = models.CharField(max_length=15, null=True, blank=True)
    bp = models.IntegerField(null=False, blank=False)
    sugar = models.IntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    credits = models.PositiveIntegerField(default=100)
    linkedin_token = models.TextField(blank=True, default='')
    expiry_date = models.DateTimeField(null=True, blank=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'gender', 'age', 'bp', 'sugar']

    def __str__(self):
        return f"{self.name} | {self.email}" 

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
