# Generated by Django 3.0.4 on 2020-03-25 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200324_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='label',
            new_name='LABEL',
        ),
    ]
