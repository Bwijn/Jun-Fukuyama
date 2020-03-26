from rest_framework import serializers
from django.utils.timezone import now

from users.models import User
from users.serializers import UserSerializer
from video.models import Banner, Video


# 轮播图
class VideoBannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = []


# 排序 推荐 (视频列表)
class VideoList(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'url', 'cover', 'title')


# 视频详情
class VideoInfoSerializer(serializers.ModelSerializer):
    # 作者头像地址
    author_avatar = serializers.CharField(source="author.avatar", read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Video
        depth = 1
        exclude = ('pub_date',)

