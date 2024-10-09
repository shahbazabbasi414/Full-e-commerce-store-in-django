# Generated by Django 5.0.6 on 2024-10-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_contact_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fabric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GSM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(blank=True, to='store.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='customizations',
            field=models.ManyToManyField(blank=True, to='store.customization'),
        ),
        migrations.AddField(
            model_name='product',
            name='fabrics',
            field=models.ManyToManyField(blank=True, to='store.fabric'),
        ),
        migrations.AddField(
            model_name='product',
            name='gsms',
            field=models.ManyToManyField(blank=True, to='store.gsm'),
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(blank=True, to='store.material'),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='store.size'),
        ),
        migrations.AddField(
            model_name='product',
            name='types',
            field=models.ManyToManyField(blank=True, to='store.type'),
        ),
    ]