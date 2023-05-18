# Generated by Django 4.1.7 on 2023-05-14 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diwe_product', '0024_image_package_image_vitrine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='scrore',
            new_name='score',
        ),
        migrations.AlterField(
            model_name='accueil',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/media/img/'),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='image1',
            field=models.ImageField(blank=True, upload_to='static/media/img/'),
        ),
        migrations.AlterField(
            model_name='accueil',
            name='image2',
            field=models.ImageField(blank=True, upload_to='static/media/img/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/img/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='package',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='diwe_product.package'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='static/media/video/'),
        ),
    ]
