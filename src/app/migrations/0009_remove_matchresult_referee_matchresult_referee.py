# Generated by Django 5.0.4 on 2024-05-18 13:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_matchresult_total_point1_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchresult',
            name='referee',
        ),
        migrations.AddField(
            model_name='matchresult',
            name='referee',
            field=models.ManyToManyField(null=True, related_name='match_result', to=settings.AUTH_USER_MODEL),
        ),
    ]
