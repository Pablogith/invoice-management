# Generated by Django 4.2 on 2023-04-07 21:08

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('contact_information', models.CharField(max_length=50)),
                ('account_status', models.CharField(choices=[(core.models.UserAccountStatus['ACTIVE'], 'active'), (core.models.UserAccountStatus['DEACTIVATED'], 'deactivated'), (core.models.UserAccountStatus['SUSPENDED'], 'suspended')], max_length=20)),
                ('role', models.CharField(choices=[(core.models.UserRole['ADMIN'], 'admin'), (core.models.UserRole['EDITOR'], 'editor'), (core.models.UserRole['VIEWER'], 'viewer')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
