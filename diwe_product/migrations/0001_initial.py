# Generated by Django 4.1.7 on 2023-04-01 18:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('reference', models.CharField(blank=True, max_length=50, unique=True)),
                ('tel1', models.CharField(blank=True, max_length=50)),
                ('tel2', models.CharField(blank=True, max_length=50, null=True)),
                ('segment', models.CharField(blank=True, choices=[('Adulte', 'Adulte'), ('Enfant', 'Enfant')], max_length=50)),
                ('pays', django_countries.fields.CountryField(max_length=2)),
                ('ville', models.CharField(blank=True, max_length=50)),
                ('code_postal', models.CharField(blank=True, max_length=10)),
                ('rue', models.CharField(blank=True, max_length=128)),
                ('numero_rue', models.CharField(blank=True, max_length=20)),
                ('commande_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('devise', models.CharField(blank=True, choices=[('EURO', 'EURO'), ('DOLLAR', 'DOLLAR')], max_length=20)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiweCategory',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DiweRegion',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='DiweRoute',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('travel_mode', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('route_lenght', models.FloatField()),
                ('duration', models.IntegerField()),
                ('is_circle', models.BooleanField()),
                ('score', models.IntegerField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tarif', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('code_postal', models.CharField(blank=True, max_length=10)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('pays', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diwe_product.pays')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diwe_product.diweregion')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('rue', models.CharField(blank=True, max_length=128)),
                ('numero_rue', models.CharField(blank=True, max_length=20)),
                ('laltitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('scrore', models.IntegerField()),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='diwe_product.diwecategory')),
                ('ville', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('package', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='diwe_product.package')),
                ('site', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='diwe_product.site')),
                ('type_service', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='diwe_product.typeservice')),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('end_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='end_sites', to='diwe_product.site')),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.diweroute')),
                ('start_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_sites', to='diwe_product.site')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('opening_time', models.DateTimeField()),
                ('closing_time', models.DateTimeField()),
                ('week_day', models.CharField(blank=True, max_length=255, null=True)),
                ('visit_duration', models.DurationField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diwe_product.site')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('nom', models.CharField(blank=True, max_length=50)),
                ('prenom', models.CharField(blank=True, max_length=50)),
                ('date_naissance', models.DateField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('commande', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.commande')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default='media/img/placeholder.png', null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='media/video/')),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.diweroute')),
                ('sequence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.sequence')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.site')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('travel_mode', models.CharField(blank=True, max_length=200, null=True)),
                ('time_between_site', models.DurationField()),
                ('distance_between_site', models.FloatField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('end_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dis_end_sites', to='diwe_product.site')),
                ('start_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dis_start_sites', to='diwe_product.site')),
            ],
        ),
        migrations.CreateModel(
            name='DetailCommande',
            fields=[
                ('prix_unitaire', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('quantite', models.IntegerField()),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('commande', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='diwe_product.commande')),
                ('package', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='diwe_product.package')),
            ],
        ),
        migrations.CreateModel(
            name='ContactSite',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('tel1', models.CharField(blank=True, max_length=64, null=True)),
                ('tel2', models.CharField(blank=True, max_length=64, null=True)),
                ('mail', models.EmailField(blank=True, max_length=200)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diwe_product.site')),
            ],
        ),
    ]
