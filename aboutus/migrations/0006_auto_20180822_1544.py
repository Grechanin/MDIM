# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-22 12:44
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0005_aboutus_tab_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True, verbose_name='Короткий опис'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='tab_title',
            field=models.TextField(blank=True, null=True, verbose_name='Заголовок закладки'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Заголовок сторінки'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
    ]