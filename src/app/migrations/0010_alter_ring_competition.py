# Generated by Django 5.0.4 on 2024-04-19 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_matchresult_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ring',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ring', to='app.competition', verbose_name='Competition'),
        ),
    ]
