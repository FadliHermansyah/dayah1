from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .import views
from profil import views as profilViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profil/', include('profil.urls')),
    path('profil_dayah/', views.profil_dayah),
    path('details/<int:pk>/', views.details, name='details'),
    path('profil_dayah/<int:pk>/', views.profil_details, name="profil_dayah"),
    path('', views.index),

]
