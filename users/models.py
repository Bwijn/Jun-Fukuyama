from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


# 重写UserManager 未使用Django自带模型类 所以创建user对象时需要自定义字段
# 重写AbstractUser里objects的 UserManager类
class ResetUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser, ):
    """自定义用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号", null=True)
    first_name = None
    last_name = None
    is_active = None
    is_staff = None
    is_superuser = None
    objects = ResetUserManager()

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    avatar = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    nickname = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'user_profile'
