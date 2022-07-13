from django.urls import  path
from .views import (main,mukellefler,personel,
                    personeller,tanimlamalar,
                    mukellef_tanımlama,sube_tanımlama,
                    mukellef_ekle,toplu_mukellef,
                    toplu_sube,personel_tanımlama,
                    personel_ekle,toplu_personel,
                    sonuc,eksikler,bordrolar,
                    bordro_sil, bordro_ekle,
                    bordro_geldi,tutanak_ekle,
                    tutanak_sil,todo_degis,todo_sil
                    )

urlpatterns = [
    path("",main,name="main"),
    path("todo/<int:todo_pk>/", todo_degis, name="todo_degis"),
    path("todo/sil/<int:todo_pk>/", todo_sil, name="todo_sil"),
    path("mukellefler/",mukellefler,name="mukellefler"),
    path("personel/<int:personel_pk>/",personel,name="personel"),
    path("personel//arama/<str:kelime>/",sonuc,name="sonuc"),
    path("personeller/",personeller,name="personeller"),
    path("bordrolar/",bordrolar,name="bordrolar"),
    path("tanimlamalar/",tanimlamalar,name="tanimlamalar"),
    path("tanimlamalar/mukellef/",mukellef_tanımlama,name="mukellef_tanımlama"),
    path("tanimlamalar/sube/",sube_tanımlama,name="sube_tanımlama"),
    path("tanimlamalar/personel/",personel_tanımlama,name="personel_tanımlama"),
    path("tanimlamalar/mukellef/ekle/",mukellef_ekle,name="mukellef_ekle"),
    path("tanimlamalar/toplu/mukellef/ekle/",toplu_mukellef,name="toplu_mukellef"),
    path("tanimlamalar/toplu/sube/ekle/",toplu_sube,name="toplu_sube"),
    path("tanimlamalar/toplu/personel/ekle/",toplu_personel,name="toplu_personel"),
    path("tanimlamalar/personel/ekle/",personel_ekle,name="personel_ekle"),
    path("tanimlamalar/personel/eksikler/",eksikler,name="eksikler"),
    path("bordro/sil/<int:bordro_pk>/<int:personel_pk>/",bordro_sil,name="bordro_sil"),
    path("bordro/ekle/<int:personel_pk>/",bordro_ekle,name="bordro_ekle"),
    path("bordro/geldi/<int:bordro_pk>/<int:personel_pk>/",bordro_geldi,name="bordro_geldi"),
    path("tutanak/ekle/<int:personel_pk>/",tutanak_ekle,name="tutanak_ekle"),
    path("tutanak/sil/<int:tutanak_pk>/<int:personel_pk>/",tutanak_sil,name="tutanak_sil"),
    
]