# Generated by Django 4.2.1 on 2023-05-19 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_customer_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='session',
        ),
    ]