# Generated by Django 2.2.4 on 2020-01-04 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0020_pengenalan_dayah_foto_profil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_lokasi',
            old_name='koordinat',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='data_lokasi',
            name='longitude',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
