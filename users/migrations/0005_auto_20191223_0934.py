# Generated by Django 3.0 on 2019-12-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_delete_likeship'),
        ('users', '0004_auto_20191220_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='like_r',
            field=models.ManyToManyField(blank=True, db_table='UserFavoriteVideo', null=True, related_name='viewer', to='video.Video'),
        ),
    ]
