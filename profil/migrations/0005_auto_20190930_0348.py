# Generated by Django 2.2.4 on 2019-09-30 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0004_auto_20190930_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kondisi_lingkungan',
            name='pendidikan_pengajar',
        ),
        migrations.AlterField(
            model_name='kesehatan',
            name='Flu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kesehatan',
            name='Lainya',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='kesehatan',
            name='batuk',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kesehatan',
            name='demam',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kesehatan',
            name='diare',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kesehatan',
            name='gatal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kondisi_lingkungan',
            name='jumlah_santri',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='kondisi_lingkungan',
            name='jumlah_santriwati',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='jumat',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='kamis',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='minggu',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='rabu',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='sabtu',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='selasa',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pendidikan',
            name='senin',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pengenalan_dayah',
            name='alamat',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='pengenalan_dayah',
            name='nama_dayah',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pengenalan_dayah',
            name='no_hp',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pengenalan_dayah',
            name='pemimpin_dayah',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pengenalan_dayah',
            name='tahun_berdiri',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='pengenalan_dayah',
            name='type_dayah',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='prestasi',
            name='santri_baca_kitabkuning',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prestasi',
            name='santri_penghafal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prestasi',
            name='santriwati_baca_kitabkuning',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prestasi',
            name='santriwati_penghafal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profil_pimpinan',
            name='pekerjaan_diluar_dayah',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='alas_tidur',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='jml_dipan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='jml_komputer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='jml_pengeras_suara',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='jml_ruangkegiatan_aula',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='kapasitas_dipan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='lainya',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='lantai_tersedia',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='luas_ruangkegiatan_aula',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='sarana_olahraga',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='sarana_tidur',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='sumber_air_untuk_mandi_cuci',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sarana_prasarana',
            name='sumber_air_untuk_minum',
            field=models.CharField(default='', max_length=200),
        ),
    ]