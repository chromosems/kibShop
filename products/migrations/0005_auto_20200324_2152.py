# Generated by Django 3.0.4 on 2020-03-24 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200324_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='LABEL',
            new_name='label',
        ),
    ]
