# Generated by Django 4.2.1 on 2023-05-30 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_remove_customer_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
