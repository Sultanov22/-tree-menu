# Generated by Django 4.0.4 on 2023-01-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menus_explicit_url_alter_menus_named_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='explicit_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menus',
            name='named_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
