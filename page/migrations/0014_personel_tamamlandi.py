# Generated by Django 4.0.3 on 2022-07-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_alter_personel_adres'),
    ]

    operations = [
        migrations.AddField(
            model_name='personel',
            name='tamamlandi',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
