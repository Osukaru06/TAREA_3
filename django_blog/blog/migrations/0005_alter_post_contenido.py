# Generated by Django 4.1 on 2023-02-25 21:57

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
