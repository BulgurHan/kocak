# Generated by Django 4.0.3 on 2022-07-09 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_personel_ise_giris_alter_personel_isten_cikis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bordro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bordro', models.FileField(upload_to='bordro')),
                ('tarih', models.DateField()),
                ('geldi', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OzlukEvrak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sozlesmesi', models.FileField(upload_to='ozluk')),
                ('gorevlendirme_belgesi', models.FileField(upload_to='ozluk')),
                ('fazla_messai_onay', models.FileField(upload_to='ozluk')),
                ('gecici_gorev_yazisi', models.FileField(upload_to='ozluk')),
                ('kimlik_fotokopisi', models.FileField(upload_to='ozluk')),
                ('adli_sicil_kaydi', models.FileField(upload_to='ozluk')),
                ('yerlesim_yeri_belgesi', models.FileField(upload_to='ozluk')),
                ('mezuniyet_belgesi', models.FileField(upload_to='ozluk')),
                ('sertifikalar', models.FileField(upload_to='ozluk')),
                ('hijyen_belgesi', models.FileField(upload_to='ozluk')),
                ('saglik_raporu', models.FileField(upload_to='ozluk')),
                ('veskikalık', models.FileField(upload_to='ozluk')),
            ],
        ),
        migrations.AddField(
            model_name='personel',
            name='meslek',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Ozluk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bordro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.bordro')),
                ('evraklar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.ozlukevrak')),
                ('personel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.personel')),
            ],
        ),
    ]
