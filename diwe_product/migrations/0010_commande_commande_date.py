# Generated by Django 4.1.7 on 2023-04-01 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0009_remove_commande_commande_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='commande_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]