# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-17 20:22
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prices',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='prices',
            name='short_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='proicecategorydescription',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True),
        ),
    ]
