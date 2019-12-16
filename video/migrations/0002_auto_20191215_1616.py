# Generated by Django 3.0 on 2019-12-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='link',
            field=models.URLField(null=True, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.URLField(verbose_name='封面URL'),
        ),
    ]
