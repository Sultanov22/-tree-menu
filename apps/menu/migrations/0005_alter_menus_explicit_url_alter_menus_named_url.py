# Generated by Django 4.0.4 on 2023-01-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menus_explicit_url_alter_menus_named_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='explicit_url',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menus',
            name='named_url',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
