# Generated by Django 4.1.7 on 2023-03-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treemenu',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
