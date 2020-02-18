# Generated by Django 2.2.4 on 2019-10-15 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0008_auto_20191008_0416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='kesehatan',
        ),
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='kondisi_lingkungan',
        ),
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='pendidikan',
        ),
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='petugas',
        ),
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='prestasi',
        ),
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='profil_pimpinan',
        ),
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='ringkasan',
        ),
        migrations.RemoveField(
            model_name='pengenalan_dayah',
            name='sarana_prasarana',
        ),
        migrations.AddField(
            model_name='ringkasan',
            name='Nama_dayah',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='profil.pengenalan_dayah', verbose_name='Nama Dayah'),
        ),
    ]
