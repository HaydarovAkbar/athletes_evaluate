# Generated by Django 5.0.4 on 2024-04-18 08:00

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_refereeuser_password_and_more'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refereeuser',
            name='ring',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referee', to='app.ring', verbose_name='Ring'),
        ),
        migrations.AlterField(
            model_name='refereeuser',
            name='username',
            field=models.CharField(max_length=6, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Enter a valid username in the format sdfsf7654', regex='^[1-9 a-z]+$')]),
        ),
    ]
