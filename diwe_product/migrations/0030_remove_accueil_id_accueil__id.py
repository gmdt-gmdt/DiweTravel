# Generated by Django 4.1.7 on 2023-05-15 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0029_alter_contactsite_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accueil',
            name='id',
        ),
        migrations.AddField(
            model_name='accueil',
            name='_id',
            field=models.AutoField(default=1, editable=False, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
