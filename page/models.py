from django.db import models


class Mukellef(models.Model):
    isim = models.CharField(
        max_length = 200,
    )
    adres = models.TextField(null=True)
    tel = models.CharField(
        max_length=11,
    )
    mail = models.EmailField()
    def __str__(self):
        return self.isim



class Sube(models.Model):
    mukellef = models.ForeignKey(
        Mukellef,
        on_delete=models.SET_NULL,
        null=True,
        )
    isim = models.CharField(
        max_length=200,
    )
    def __str__(self):
        return "{} - {}".format(self.isim,self.mukellef)




class Personel(models.Model):
    mukellef = models.ForeignKey(
        Mukellef,
        on_delete=models.SET_NULL,
        null=True,
    )
    sube = models.ForeignKey(
        Sube,
        on_delete=models.SET_NULL,
        null=True,
    )
    isim = models.CharField(
        max_length=200,
    )
    tc = models.PositiveBigIntegerField()
    meslek = models.CharField(
        max_length=100,
        null=True,
    )
    adres = models.TextField(
        null=True,
        blank=True
    )
    ise_giris = models.DateTimeField(
        null=True,
        blank=True
    )
    isten_cikis = models.DateTimeField(
        null=True,
        blank=True
    )
    tamamlandi = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return self.isim




class Bordro(models.Model):
    personel = models.ForeignKey(
        Personel,
        on_delete=models.SET_NULL,
        null=True,
    )
    tarih = models.DateField()
    geldi = models.BooleanField(
        default=False,
    )

class Tutanak(models.Model):
    personel = models.ForeignKey(
        Personel,
        on_delete=models.SET_NULL,
        null=True,
    )
    baslik = models.CharField(max_length=200,null=True)
    tarih = models.DateField(null=True)



class Ozluk(models.Model):
    personel = models.ForeignKey(
        Personel,
        on_delete= models.SET_NULL,
        null = True,
    )
    is_sozlesmesi = models.BooleanField(default=False)
    gorevlendirme_belgesi = models.BooleanField(default=False)
    fazla_messai_onay = models.BooleanField(default=False)
    gecici_gorev_yazisi = models.BooleanField(default=False)
    kimlik_fotokopisi = models.BooleanField(default=False)
    adli_sicil_kaydi = models.BooleanField(default=False)
    yerlesim_yeri_belgesi = models.BooleanField(default=False)
    mezuniyet_belgesi = models.BooleanField(default=False)
    sertifikalar = models.BooleanField(default=False)
    hijyen_belgesi = models.BooleanField(default=False)
    saglik_raporu = models.BooleanField(default=False)
    veskikalık =  models.BooleanField(default=False)
    istifa = models.BooleanField(default=False)

    def __str__(self):
        return self.personel.isim




class ToDo(models.Model):
    aciklama = models.TextField()
    ok = models.BooleanField(
        default=False,
    )
