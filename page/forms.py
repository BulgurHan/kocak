from django import forms
from .models import Mukellef, Ozluk, Personel, Sube,Bordro



class GirisForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Kullanıcı Adınız'
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control ',
                'placeholder': 'Şifreniz'
            }
        )
    )

class MukellefForm(forms.ModelForm):
    isim = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"İsim"
        })
    )
    adres = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Adres"
        })
    )
    mail = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Mail"
        })
    )
    tel = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder":"Telefon"
        })
    )
    class Meta:
        model = Mukellef
        fields = [
            'isim','adres','mail','tel'
        ]


class SubeForm(forms.ModelForm):
    class Meta:
        model = Sube
        fields = ['mukellef', 'isim']


class PersonelForm(forms.ModelForm):
    class Meta:
        model = Personel
        fields = ['mukellef','sube','isim','meslek','tc','adres','ise_giris','isten_cikis']
    def __init__(self, *args, **kwargs):
        super(PersonelForm, self).__init__(*args, **kwargs)
        self.fields['isten_cikis'].required = False


class OzlukForm(forms.ModelForm):
    is_sozlesmesi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    gorevlendirme_belgesi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    fazla_messai_onay = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    gecici_gorev_yazisi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    kimlik_fotokopisi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    adli_sicil_kaydi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    yerlesim_yeri_belgesi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    mezuniyet_belgesi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    sertifikalar = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    hijyen_belgesi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    saglik_raporu = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    veskikalık = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    istifa = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))           
    class Meta:
        model = Ozluk
        fields = ['is_sozlesmesi','gorevlendirme_belgesi','fazla_messai_onay','gecici_gorev_yazisi','kimlik_fotokopisi',
        'adli_sicil_kaydi','yerlesim_yeri_belgesi','mezuniyet_belgesi',"sertifikalar","hijyen_belgesi","saglik_raporu",
        "veskikalık","istifa"]
    def __init__(self, *args, **kwargs):
        super(OzlukForm, self).__init__(*args, **kwargs)
        self.fields['is_sozlesmesi'].required = False
        self.fields['gorevlendirme_belgesi'].required = False
        self.fields['fazla_messai_onay'].required = False
        self.fields['gecici_gorev_yazisi'].required = False
        self.fields['kimlik_fotokopisi'].required = False
        self.fields['adli_sicil_kaydi'].required = False
        self.fields['yerlesim_yeri_belgesi'].required = False
        self.fields['mezuniyet_belgesi'].required = False
        self.fields['sertifikalar'].required = False
        self.fields['hijyen_belgesi'].required = False
        self.fields['saglik_raporu'].required = False
        self.fields['veskikalık'].required = False
        self.fields['istifa'].required = False

class AramaForm(forms.Form):
    kelime = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Personellerde Ara..'
            }
        )
    )



class BordroForm(forms.Form):
    tarih = forms.DateField(
        widget= forms.DateInput(
            attrs={
                'class' :'form-control',
                'placeholder': 'Gün/Ay/Yıl',
                'id': 'datepicker-autoclose'
            }
            )
        )
    geldi = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class':"form-check-input"
    }))
    def __init__(self, *args, **kwargs):
        super(BordroForm, self).__init__(*args, **kwargs)
        self.fields['geldi'].required = False


class TutanakForm(forms.Form):
    tarih = forms.DateField(
        widget= forms.DateInput(
            attrs={
                'class' :'form-control',
                'placeholder': 'Gün/Ay/Yıl',
                'id': 'datepicker-autoclose'
            }
            )
        )
    baslik = forms.CharField(widget=forms.TextInput(attrs={
        'class':"form-control"
    }))
    def __init__(self, *args, **kwargs):
        super(TutanakForm, self).__init__(*args, **kwargs)
        self.fields['tarih'].required = False
        self.fields['baslik'].required = False


class ToDoForm(forms.Form):
    aciklama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
        )



