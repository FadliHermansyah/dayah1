from django.shortcuts import render
from .models import ringkasan,petugas,profil_pimpinan,kondisi_lingkungan,pendidikan,prestasi,kesehatan,sarana_prasarana,pengenalan_dayah,data_lokasi,data_foto

def index(request):
    context = {
        'title':'Profil',
        'heading':'DATA DAYAH',
        'subheading':'Kabupaten Aceh Tengah',
        'nav': [
            ['/' , 'Home'],
            ['/profil','Profil'],
            ['/about','About']
        ],
        'ringkasan' : ringkasan.objects.all,
        'luas' : kondisi_lingkungan.objects.all,
        'nbar': 'dayah'
    }
    return render(request,'profil/index.html', context)