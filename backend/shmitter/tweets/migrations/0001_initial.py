# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-05 08:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=140, verbose_name='body')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'tweet',
                'verbose_name_plural': 'tweets',
                'ordering': ['-created'],
            },
        ),
    ]
