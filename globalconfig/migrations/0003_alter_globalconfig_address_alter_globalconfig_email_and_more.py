# Generated by Django 5.0.2 on 2024-02-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalconfig', '0002_alter_globalconfig_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalconfig',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección para documentos'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email para documentos'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='Logo de la app'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='logo_documents',
            field=models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='Logo para documentos'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='name',
            field=models.CharField(blank=True, default='Georut', max_length=100, null=True, verbose_name='Nombre de la app'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='name_documents',
            field=models.CharField(max_length=100, verbose_name='Nombre para documentos'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Identificador para documentos'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono para documentos'),
        ),
        migrations.AlterField(
            model_name='globalconfig',
            name='web',
            field=models.URLField(blank=True, null=True, verbose_name='Web para documentos'),
        ),
    ]
