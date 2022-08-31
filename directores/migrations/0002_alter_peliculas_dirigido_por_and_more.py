# Generated by Django 4.1 on 2022-08-28 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='dirigido_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='directores.directores'),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='sinopsis',
            field=models.TextField(help_text='Escribe la sinopsis de la película', max_length=500),
        ),
    ]
