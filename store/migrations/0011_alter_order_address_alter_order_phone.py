# Generated by Django 5.0.6 on 2024-08-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_address_order_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=11),
        ),
    ]
