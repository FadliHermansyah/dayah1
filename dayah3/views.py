from django.shortcuts import get_object_or_404, render
from profil.models import ringkasan,petugas,profil_pimpinan,kondisi_lingkungan,pendidikan,prestasi,kesehatan,sarana_prasarana,pengenalan_dayah,data_lokasi,data_foto

# def book_update(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return save_book_form(request, form, 'books/includes/partial_book_update.html')
  
# def index(request):
#     context = {
#         'title':'Kominfo Dayah',
#         'heading':'PROFIL DAYAH',
#         'subheading':'Provinsi Aceh Tengah',
#         'nav': [
#             ['/' , 'Home'],
#             ['/profi','Profil'],
#             ['/about','About']
#         ],
#         'dayah' : pengenalan_dayah.objects.all,
#         'ringkasan' : ringkasan.objects.all,
#         'pendidikan' : get_object_or_404(pendidikan, nama_dayah=4),
#         'foto' : data_foto.objects.all,
#     }
#     return render(request,'index.html',context) , 'pendidik' : pendidikan 

def index(request):
    dayah = pengenalan_dayah.objects.all
    ringkasn = ringkasan.objects.all

    return render(request,'index.html', { 'dayah' : dayah, 'ringkasn' : ringkasan , 'nbar': 'home'})

def details(request, pk):
    ID = pk
    dayahn = pengenalan_dayah.objects.get(id=ID)
    pendidik = pendidikan.objects(nama_dayah_id=ID)
    # pendidik = get_object_or_404(pendidikan, nama_dayah_id=ID)

    return render(request,'index.html', { 'dayahn' : dayahn, 'pendidik' : pendidik })

def profil_details(request, pk):
    ID = pk
    dayah = pengenalan_dayah.objects.get(id=ID)
    ringkasn = ringkasan.objects.get(nama_dayah_id=ID)
    pendidik = pendidikan.objects.get(nama_dayah_id=ID)
    santri = kondisi_lingkungan.objects.get(nama_dayah_id=ID)
    lokasi = data_lokasi.objects.get(nama_dayah_id=ID)
    prestasis = prestasi.objects.get(nama_dayah_id=ID)
    sarana = sarana_prasarana.objects.get(nama_dayah_id=ID)
    sehat = kesehatan.objects.get(nama_dayah_id=ID)

    return render(request, 'testpk.html', 
                                        { 'nbar': 'dayah', 
                                        'dayah' : dayah, 
                                        'pendidik' : pendidik, 
                                        'ringkasn' : ringkasn, 
                                        'santri' : santri, 
                                        'lokasi' : lokasi, 
                                        'prestasis' : prestasis,
                                        'sarana' : sarana,
                                        'kesehatan' : sehat})

def profil_dayah(request):
    # context = {
    #     'pengenalan_dayah' : pengenalan_dayah.object.raw(),
    # }
    return render(request, 'profil_umum.html')
