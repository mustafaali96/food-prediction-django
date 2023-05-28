# Generated by Django 4.1.8 on 2023-05-13 11:18

import django.core.validators
from django.db import migrations, models
import revoke_app.models.others


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(default=revoke_app.models.others.generate_uuid, editable=False, max_length=32, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(message="Given value doesn't meet the pattern requirements", regex='^(?=.{3,15})[a-zA-Z ]*$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('bp', models.CharField(choices=[('Healthy', 'Healthy'), ('Elevated', 'Elevated'), ('Stage 1 Hypertension', 'Stage One Hypertension'), ('Stage 2 Hypertension', 'Stage Two Hypertension'), ('Hypertension Crisis', 'Hypertension Crisis')], max_length=50)),
                ('sugar', models.CharField(choices=[('Normal', 'Normal'), ('Pre-diabetes', 'Pre Diabetes'), ('Diabetes', 'Diabetes')], max_length=50)),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.RegexValidator(message="Given value doesn't meet the pattern requirements", regex='^(?=.{11,13})\\d+$')])),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
