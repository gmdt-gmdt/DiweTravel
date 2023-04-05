# Generated by Django 4.1.7 on 2023-04-01 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0010_commande_commande_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='devise',
            field=models.CharField(blank=True, choices=[('EURO', 'EURO'), ('DOLLAR', 'DOLLAR')], max_length=20),
        ),
        migrations.AddField(
            model_name='commande',
            name='segment',
            field=models.CharField(blank=True, choices=[('Adulte', 'Adulte'), ('Enfant', 'Enfant')], max_length=50),
        ),
    ]
