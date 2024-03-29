# Generated by Django 5.0.2 on 2024-02-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Georut', max_length=100, verbose_name='name_of_company')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='logo_of_company')),
                ('number', models.CharField(blank=True, max_length=20, null=True, verbose_name='number_of_company')),
                ('name_documents', models.CharField(max_length=100, verbose_name='name_of_documents')),
                ('logo_documents', models.ImageField(blank=True, null=True, upload_to='logos', verbose_name='logo_of_documents')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address_of_company')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='phone_of_company')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email_of_company')),
                ('web', models.URLField(blank=True, null=True, verbose_name='web_of_company')),
            ],
        ),
    ]
