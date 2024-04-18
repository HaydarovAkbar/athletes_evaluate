# Generated by Django 5.0.4 on 2024-04-18 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_refereeuser_ring_alter_refereeuser_username'),
        ('app', '0003_alter_matchresult_referee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.RegexValidator(code='invalid_password', message='Enter a valid password in the format 1234567654', regex='^[1-9]+$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=6, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Enter a valid username in the format sdfsf7654', regex='^[1-9 a-z]+$')]),
        ),
        migrations.DeleteModel(
            name='RefereeUser',
        ),
    ]
