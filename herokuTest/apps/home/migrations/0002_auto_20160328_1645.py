# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 19:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slideritem',
            name='image',
        ),
        migrations.RemoveField(
            model_name='slideritemlink',
            name='sliderItem',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='SliderItem',
        ),
        migrations.DeleteModel(
            name='SliderItemLink',
        ),
    ]
