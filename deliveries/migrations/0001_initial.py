# Generated by Django 4.2.3 on 2023-07-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=32)),
                ('delivery_person', models.CharField(max_length=32)),
                ('recipient_name', models.CharField(max_length=32)),
                ('delivery_order_number', models.CharField(max_length=32)),
            ],
        ),
    ]
