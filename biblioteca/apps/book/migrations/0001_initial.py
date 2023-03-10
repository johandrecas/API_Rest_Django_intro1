# Generated by Django 4.1.7 on 2023-03-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=34, verbose_name='Apellido')),
                ('nacionalidad', models.CharField(max_length=45, verbose_name='Nacionalidad')),
                ('estado', models.BooleanField(default=True)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Modelo2',
                'verbose_name_plural': 'Modelos2',
            },
        ),
    ]
