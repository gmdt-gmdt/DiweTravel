# Generated by Django 4.1.7 on 2023-04-01 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0006_alter_commande_commande_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='pays',
        ),
    ]
