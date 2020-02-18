from django.contrib import admin
from .models import ringkasan,petugas,profil_pimpinan,kondisi_lingkungan,pendidikan,prestasi,kesehatan,sarana_prasarana,pengenalan_dayah,data_lokasi,data_foto

class ringkasanInline(admin.TabularInline):
    model = ringkasan
    min_num = 1
    max_num = 1
    extra = 0

class petugasInline(admin.TabularInline):
    model = petugas
    min_num = 1
    max_num = 1

class profil_pimpinanInline(admin.TabularInline):
    model = profil_pimpinan
    min_num = 1
    max_num = 1

class kondisi_lingkunganInline(admin.TabularInline):
    model = kondisi_lingkungan
    min_num = 1
    max_num = 1

class pendidikanInline(admin.StackedInline):
    model = pendidikan
    min_num = 1
    max_num = 1

class prestasiInline(admin.TabularInline):
    model = prestasi
    min_num = 1
    max_num = 1

class kesehatanInline(admin.TabularInline):
    model = kesehatan
    min_num = 1
    max_num = 1

class sarana_prasaranaInline(admin.StackedInline):
    model = sarana_prasarana
    min_num = 1
    max_num = 1

class data_lokasiInline(admin.TabularInline):
    model = data_lokasi
    min_num = 1
    max_num = 1

class data_fotoInline(admin.TabularInline):
    model = data_foto
    min_num = 1
    max_num = 10


class AdminDayah(admin.ModelAdmin):
    inlines =[
        ringkasanInline,
        petugasInline,
        profil_pimpinanInline,
        kondisi_lingkunganInline,
        pendidikanInline,
        prestasiInline,
        kesehatanInline,
        sarana_prasaranaInline,
        data_lokasiInline,
        data_fotoInline
    ]


admin.site.site_header = 'Admin Profil Dayah 1.0'
admin.site.register(pengenalan_dayah, AdminDayah)