# Generated by Django 4.2.1 on 2023-06-02 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0009_customer_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]