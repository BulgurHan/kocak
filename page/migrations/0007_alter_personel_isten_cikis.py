# Generated by Django 4.0.3 on 2022-07-10 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_ozlukevrak_istifa_tutanak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personel',
            name='isten_cikis',
            field=models.DateField(blank=True, null=True),
        ),
    ]
