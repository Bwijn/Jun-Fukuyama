# Generated by Django 3.0 on 2019-12-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(help_text='URL', max_length=128, null=True, verbose_name='URL'),
        ),
    ]
