# Generated by Django 5.0.2 on 2024-02-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalconfig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalconfig',
            name='name',
            field=models.CharField(blank=True, default='Georut', max_length=100, null=True, verbose_name='name_of_company'),
        ),
    ]
