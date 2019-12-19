from rest_framework import serializers
from django.utils.timezone import now

from users.models import User
from users.serializers import UserSerializer
from video.models import Banner, Video, LikeShip


# 轮播图
class VideoBannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


# 首页推荐
class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


# 视频详情
class VideoInfoSerializer(serializers.ModelSerializer):
    # 作者头像地址
    author_avatar = serializers.CharField(source="author.avatar", read_only=True)
    author = UserSerializer(read_only=True)
    # 点赞数量
    # like = serializers.PrimaryKeyRelatedField(queryset=LikeShip.objects.all())

    class Meta:
        model = Video
        depth = 1
        exclude = ( 'pub_date',)


# 视频点赞 中间表的序列化器
class VideoFavorite(serializers.ModelSerializer):
    video = serializers.PrimaryKeyRelatedField(
        queryset=Video.objects.all())
    Viewer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all())

    class Meta:
        model = LikeShip
        read_only_fields = ('id',)
        fields = "__all__"
