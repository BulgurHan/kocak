# Generated by Django 4.0.3 on 2022-07-09 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_bordro_ozlukevrak_personel_meslek_ozluk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ozluk',
            name='bordro',
        ),
        migrations.AddField(
            model_name='bordro',
            name='personel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.personel'),
        ),
    ]
