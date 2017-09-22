# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('text', models.TextField(max_length=500, null=True, blank=True)),
                ('pdffile', models.FileField(upload_to=b'media/files')),
                ('image', models.ImageField(upload_to=b'media/images')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'modified')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('is_active', models.BooleanField()),
                ('is_authenticated', models.BooleanField()),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.BooleanField()),
            ],
        ),
    ]
