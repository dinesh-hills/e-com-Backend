# Generated by Django 4.1.3 on 2022-11-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
