# Generated by Django 3.1.7 on 2021-02-26 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='bio',
            new_name='about',
        ),
    ]