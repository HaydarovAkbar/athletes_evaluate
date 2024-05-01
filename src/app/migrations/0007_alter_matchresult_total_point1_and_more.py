# Generated by Django 5.0.4 on 2024-04-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_matchresult_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchresult',
            name='total_point1',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='total_point2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='user1_point',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='matchresult',
            name='user2_point',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
