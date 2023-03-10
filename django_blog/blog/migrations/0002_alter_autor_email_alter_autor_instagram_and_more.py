# Generated by Django 4.1 on 2023-02-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='web',
            field=models.URLField(blank=True, null=True, verbose_name='Web'),
        ),
    ]
