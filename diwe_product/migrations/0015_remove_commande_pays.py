# Generated by Django 4.1.7 on 2023-04-01 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0014_rename_country_commande_pays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='pays',
        ),
    ]
