# Generated by Django 5.0.6 on 2024-10-09 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_color_customization_fabric_gsm_material_size_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.material'),
        ),
    ]
