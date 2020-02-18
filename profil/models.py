from django.db import models
from multiselectfield import MultiSelectField
from datetime import date

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return "{}".format(self.title)

class pengenalan_dayah(models.Model):
    nama_dayah = models.CharField(max_length=50, default="")
    alamat = models.CharField(max_length=250, default="")
    pemimpin_dayah = models.CharField(max_length=50, default="")
    tahun_berdiri = models.CharField(max_length=50, default="")
    no_hp = models.CharField(max_length=50, default="", blank=True, null=True)
    type_dayah = models.CharField(max_length=50, default="")
    foto_profil = models.ImageField(upload_to='static/profil_img/', blank='true')
    def __str__(self):
        return "{}".format(self.nama_dayah)
    class Meta:
        verbose_name = ('FORM DAYAH')

class ringkasan(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    jumlah_pekerja = models.CharField(max_length=50)
    smp = models.IntegerField(default=0)
    sma = models.IntegerField(default=0)
    s1 = models.IntegerField(default=0)
    s2 = models.IntegerField(default=0)
    s3 = models.IntegerField(default=0)
    # images = models.ImageField(upload_to='profil_img', blank='true')

class petugas(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    nama_petugas = models.CharField(max_length=50)
    nama_koordinator = models.CharField(max_length=50)
    nama_pemberi_informasi = models.CharField(max_length=50, default="", blank=True, null=True)
    tgl_pelaksanaan = models.DateField(default=date.today)
    tgl_pemeriksaan = models.DateField(default=date.today)

class profil_pimpinan(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    nama_pimpinan = models.CharField(max_length=50)
    pendidikan = models.CharField(max_length=100)
    jumlah_keluarga = models.IntegerField()
    pekerjaan_diluar_dayah = models.CharField(max_length=50, default="", blank=True, null=True)

class kondisi_lingkungan(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    luas_tanah = models.IntegerField()
    jumlah_santri = models.IntegerField(default=0)
    jumlah_santriwati = models.IntegerField(default=0)
    jarak_pemukiman = models.IntegerField(default=0)
    jumlah_kk_sekitar = models.IntegerField(default=0)
    
class pendidikan(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    formal = models.IntegerField(default=0)
    non_formal = models.IntegerField(default=0)
    pendidikan = (('Tahfiz / Hafiz', 'Tahfiz / Hafiz'),('Kitab Kuning', 'Kitab Kuning'))
    jenis_pendidikan = MultiSelectField(choices = pendidikan)
    senin = models.CharField(max_length=50, default="", blank=True, null=True)
    selasa = models.CharField(max_length=50, default="", blank=True, null=True)
    rabu = models.CharField(max_length=50, default="", blank=True, null=True)
    kamis = models.CharField(max_length=50, default="", blank=True, null=True)
    jumat = models.CharField(max_length=50, default="", blank=True, null=True)
    sabtu = models.CharField(max_length=50, default="", blank=True, null=True)
    minggu = models.CharField(max_length=50, default="", blank=True, null=True)

class prestasi(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    santri_penghafal = models.IntegerField(default=0)
    santriwati_penghafal = models.IntegerField(default=0) 
    santri_baca_kitabkuning = models.IntegerField(default=0) 
    santriwati_baca_kitabkuning = models.IntegerField(default=0) 

class kesehatan(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    diare = models.IntegerField(default=0)
    gatal = models.IntegerField(default=0)
    demam = models.IntegerField(default=0)
    batuk = models.IntegerField(default=0)
    Flu = models.IntegerField(default=0)
    Lainya = models.CharField(max_length=100, default="", blank=True, null=True)
    
class sarana_prasarana(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    jml_kantor = models.IntegerField(default=0)
    jml_perpustakaan = models.IntegerField(default=0)
    jml_kamarguru = models.IntegerField(default=0)
    jml_kelas_santri = models.IntegerField(default=0)
    jml_kelas_santriwati = models.IntegerField(default=0)
    kapasitas_siswa_perkelas = models.IntegerField(default=0)
    jml_kamar_santri = models.IntegerField(default=0)
    jml_kamar_santriwati = models.IntegerField(default=0)
    jml_kamar_tamu = models.IntegerField(default=0)
    jml_mushola = models.IntegerField(default=0)
    jml_dapur_umum = models.IntegerField(default=0)
    jml_ruang_makan = models.IntegerField(default=0)
    jml_ruangkegiatan_aula = models.IntegerField(default=0)
    jml_komputer = models.IntegerField(default=0)
    jml_pengeras_suara = models.IntegerField(default=0)
    lainya = models.CharField(max_length=100, default="", blank=True, null=True)
    sumber_air_untuk_minum = models.CharField(max_length=200, default="", blank=True, null=True)
    sumber_air_untuk_mandi_cuci = models.CharField(max_length=200, default="", blank=True, null=True)
    jml_kamar_madi = models.IntegerField(default=0)
    jml_kantin = models.IntegerField(default=0)
    sarana_olahraga = models.CharField(max_length=200, default="", blank=True, null=True)
    jml_tempat_wudhu = models.IntegerField(default=0)
    sarana_tidur = models.CharField(max_length=200, default="", blank=True, null=True)
    jml_dipan = models.IntegerField(default=0)
    kapasitas_dipan = models.IntegerField(default=0)
    tidak_menggunakan_dipan = models.BooleanField(default=0)
    alas_tidur = models.CharField(max_length=200,  default="", blank=True, null=True)
    lantai_tersedia = models.CharField(max_length=100, default="", blank=True, null=True)

class data_lokasi(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    latitude = models.CharField(max_length=100, default="", blank=True, null=True)
    longitude = models.CharField(max_length=100, default="", blank=True, null=True)

class data_foto(models.Model):
    nama_dayah = models.ForeignKey(pengenalan_dayah, on_delete=models.CASCADE, default=1)
    foto = models.ImageField(upload_to='profil/static/img/profil_img', blank='true')
    
