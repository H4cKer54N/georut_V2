# Generated by Django 5.0.2 on 2024-02-29 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('globalconfig', '0005_alter_globalconfig_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='globalconfig',
            options={'default_permissions': (), 'permissions': [('view_global_conf', 'Can view global conf'), ('change_global_conf', 'Can change global conf'), ('delete_global_conf', 'Can delete global conf'), ('add_global_conf', 'Can add global conf')], 'verbose_name': 'Global config', 'verbose_name_plural': 'Global Configs'},
        ),
    ]
