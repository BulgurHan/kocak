# Generated by Django 4.0.3 on 2022-07-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_alter_personel_isten_cikis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personel',
            name='ise_giris',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='personel',
            name='isten_cikis',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
