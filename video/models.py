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
    classification = models.ForeignKey(Classification, blank=True, on_delete=models.SET_NULL, null=True)  # 分类
    animename = models.CharField(max_length=200, null=True, blank=True)  # 番名 todo 改外键

    director = models.ForeignKey(to='video.Director', related_name='production', blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'video'

    def __str__(self):
        return self.title


# 剧集数
class Episode(models.Model):
    url = models.CharField(max_length=500, null=True, blank=True)  # 每一集的url
    episode_num = models.CharField(max_length=500, null=True, )  # 剧集的名字
    video_obj = models.ForeignKey(to="video.Video", related_name='episodes', on_delete=models.CASCADE)  # 所属的视频

    class Meta:
        db_table = "Episode"


# 视频分类表
class Type(models.Model):
    # 类名
    name = models.CharField(max_length=500, null=True, blank=True)  # 分类名
    # 此类下的视频
    videos = models.ManyToManyField('video.Video', db_table="TypeToVideo", related_name="type", blank=True, )
    # list = models.ManyToManyField('video.Video', db_table='UserFavoriteVideo', related_name='viewer', blank=True, )


# 视频导演表
class Director(models.Model):
    # 导演名字
    name = models.CharField(max_length=500, null=True, blank=True, )  # 名

    class Meta:
        db_table = "Director"


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
