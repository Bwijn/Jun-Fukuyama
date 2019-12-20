from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    nickname = models.CharField(max_length=30)
    # 头像url
    avatar = models.CharField(verbose_name="URL", help_text="URL", max_length=128, null=True)

    like_r = models.ManyToManyField('video.Video', db_table='UserFavoriteVideo', related_name='viewer')
    # 暂时重写创建user 管理员与员工身份字段暂无
    # objects = ResetUserManager()
    # class Meta:
    #     db_table = "u"
