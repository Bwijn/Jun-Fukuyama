from datetime import datetime

from django.db import models


# Create your models here.


# 番名
class VideoName(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "AnimeName"


# 视频分类 Cover ...
class Classification(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "v_classification"


# 视频详情
class Video(models.Model):
    # 一对多 User 对 Video
    url = models.CharField(max_length=500, null=True, blank=True)  # 视频地址
    author = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, null=True, blank=True)  # 作者
    cover = models.CharField(max_length=500, null=True, blank=True)  # 封面
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # 发布日期
    brief = models.TextField(default=None, null=True, blank=True)  # 视频简介
    title = models.CharField(max_length=500, null=True, blank=True)  # 视频标题
    view_count = models.IntegerField(default=0, blank=True)  # 观看次数
    classification = models.ForeignKey(Classification, blank=True, on_delete=models.CASCADE, null=True)  # 分类
    episode = models.PositiveIntegerField(null=True, blank=True)  # 集数
    animename = models.CharField(max_length=200, null=True, blank=True)  # 番名 todo 改外键

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
