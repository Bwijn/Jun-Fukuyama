from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager


# 重写创建对象方法 不再有管理员字段
class ResetUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)


# 用户表
class User(AbstractUser):
    # first_name = None
    # last_name = None
    nickname = models.CharField(max_length=30)

    # 暂时重写创建user 管理员与员工身份字段暂无
    # objects = ResetUserManager()
    # class Meta:
    #     db_table = "u"

