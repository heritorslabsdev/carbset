# Generated by Django 4.2.1 on 2024-04-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product_authorized_project_designee_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='documents',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
