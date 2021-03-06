# Generated by Django 4.0.3 on 2022-07-09 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ozlukevrak',
            name='istifa',
            field=models.FileField(null=True, upload_to='ozluk'),
        ),
        migrations.CreateModel(
            name='Tutanak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutanak', models.FileField(upload_to='tutanak')),
                ('personel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.personel')),
            ],
        ),
    ]
