# Generated by Django 4.1.4 on 2022-12-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_customer_email_remove_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': [('view_history', 'Can view history')]},
        ),
    ]
