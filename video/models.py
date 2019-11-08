from django.db import models

# Create your models here.
from users.models import User


class Video(models.Model):
    # 一对多 User 对 Video
    url = models.CharField(max_length=500)  # 视频地址
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # 作者
    cover = models.CharField(max_length=500)  # 封面
    pub_date = models.DateTimeField(auto_now_add=True)  # 发布日期

    class Meta:
        db_table = 'video'
