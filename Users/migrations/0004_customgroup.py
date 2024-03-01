# Generated by Django 5.0.2 on 2024-03-01 08:21

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_user_options_alter_historicaluser_address_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'permissions': [('view_group', 'Can view group'), ('change_group', 'Can change group'), ('delete_group', 'Can delete group'), ('add_group', 'Can add group')],
                'default_permissions': (),
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
