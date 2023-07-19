# Generated by Django 4.2.3 on 2023-07-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaser_name', models.CharField(max_length=32)),
                ('purchaser_number', models.CharField(max_length=32)),
                ('vendor_name', models.CharField(max_length=32)),
                ('vender_number', models.CharField(max_length=32)),
                ('product_description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]