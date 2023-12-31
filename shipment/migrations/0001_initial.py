# Generated by Django 4.2.3 on 2023-07-15 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tracking_number', models.CharField(max_length=50, unique=True)),
                ('recipient_address', models.CharField(max_length=200)),
                ('recipient_contact_info', models.CharField(max_length=100)),
            ],
        ),
    ]
