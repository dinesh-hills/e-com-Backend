# Generated by Django 4.1.3 on 2022-11-21 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_address_pincode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unit_price',
        ),
    ]
