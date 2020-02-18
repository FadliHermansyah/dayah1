# Generated by Django 2.2.4 on 2019-10-31 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0015_auto_20191023_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_lokasi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koordinat', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('nama_dayah', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profil.pengenalan_dayah')),
            ],
        ),
        migrations.CreateModel(
            name='data_foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank='true', upload_to='profil_img')),
                ('nama_dayah', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profil.pengenalan_dayah')),
            ],
        ),
    ]