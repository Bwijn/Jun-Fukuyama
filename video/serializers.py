from rest_framework import serializers
from django.utils.timezone import now

from users.models import User
from users.serializers import UserSerializer
from video.models import Banner, Video, Episode, Type


# 排序 推荐 (视频列表)
class VideoList(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'url', 'cover', 'title', 'view_count')


#  分类 序列化器
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        depth = 1
        fields = '__all__'
        # fields = ['name', ]

    # 重写返回数据
    def to_representation(self, value):
        """
        重写方法 使返回指定数据
         "type": [
            "日剧",
            "日本动漫"
        ],
        :param value:
        :return:
        """
        print(value.name)
        return value.name


# 视频详情 API  Details Page [分类] [主演] [剧情介绍]
class VideoInfoSerializer(serializers.ModelSerializer):
    # 作者头像地址
    # author_avatar = serializers.CharField(source="author.avatar", read_only=True)
    # author = UserSerializer(read_only=True)
    """
    type fields 在这里需要显示定义  否则 需要在fields = [...] 里面声明
    """
    type = TypeSerializer(many=True)

    class Meta:
        model = Video
        depth = 1
        exclude = ['view_count', 'author', 'animename', 'classification', ]


# 分集 序列化器
class EpisodeDetails(serializers.ModelSerializer):
    class Meta:
        model = Episode
        depth = 0
        fields = ['episode_num', 'url', 'video_obj']
        # fields = '__all__'
