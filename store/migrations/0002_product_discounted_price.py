# Generated by Django 5.0.6 on 2024-08-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Discounted_price',
            field=models.IntegerField(default=0),
        ),
    ]
