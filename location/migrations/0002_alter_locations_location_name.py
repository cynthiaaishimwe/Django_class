# Generated by Django 4.2.1 on 2023-06-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='location_name',
            field=models.CharField(max_length=32),
        ),
    ]
