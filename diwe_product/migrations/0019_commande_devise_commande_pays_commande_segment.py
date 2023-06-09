# Generated by Django 4.1.7 on 2023-04-02 17:25

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0018_remove_commande_devise_remove_commande_segment'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='devise',
            field=models.CharField(blank=True, choices=[('EURO', 'EURO'), ('DOLLAR', 'DOLLAR')], max_length=20),
        ),
        migrations.AddField(
            model_name='commande',
            name='pays',
            field=django_countries.fields.CountryField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commande',
            name='segment',
            field=models.CharField(blank=True, choices=[('Adulte', 'Adulte'), ('Enfant', 'Enfant')], max_length=50),
        ),
    ]
