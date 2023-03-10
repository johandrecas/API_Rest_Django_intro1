# Generated by Django 4.1.7 on 2023-03-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_alter_libro_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'libro__', 'verbose_name_plural': 'libros__'},
        ),
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha Creacion'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha Creacion'),
        ),
    ]
