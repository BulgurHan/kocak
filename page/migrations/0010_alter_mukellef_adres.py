# Generated by Django 4.0.3 on 2022-07-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_remove_ozluk_evraklar_ozluk_adli_sicil_kaydi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mukellef',
            name='adres',
            field=models.TextField(null=True),
        ),
    ]
