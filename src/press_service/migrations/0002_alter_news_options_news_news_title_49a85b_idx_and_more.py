# Generated by Django 5.0.4 on 2024-04-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AddIndex(
            model_name='news',
            index=models.Index(fields=['title', 'created_at'], name='news_title_49a85b_idx'),
        ),
        migrations.AlterModelTable(
            name='news',
            table='news',
        ),
    ]
