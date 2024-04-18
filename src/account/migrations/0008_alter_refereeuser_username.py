# Generated by Django 5.0.4 on 2024-04-17 09:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_refereeuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refereeuser',
            name='username',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_login', message='Enter a valid registration number in the format 1234567654', regex='^[1-9 a-z]+$')]),
        ),
    ]