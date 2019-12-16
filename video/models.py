from datetime import datetime

from django.db import models

# Create your models here.
from users.models import User


# 视频分类
class Classification(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "v_classification"


# 视频信息表
class Video(models.Model):
    # 一对多 User 对 Video
    url = models.CharField(max_length=500)  # 视频地址
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # 作者
    cover = models.CharField(max_length=500)  # 封面
    pub_date = models.DateTimeField(auto_now_add=True)  # 发布日期
    brief = models.TextField(default=None)  # 视频简介
    title = models.CharField(max_length=500)  # 视频标题
    view_count = models.IntegerField(default=0)  # 观看次数
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True)  # 分类

    class Meta:
        db_table = 'video'


# 轮播图数据表
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    cover_url = models.URLField(max_length=500, verbose_name=u"封面URL", null=True)
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    link = models.URLField(max_length=200, verbose_name=u"链接", null=True)

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
