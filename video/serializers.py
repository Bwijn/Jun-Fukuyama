from rest_framework import serializers
from django.utils.timezone import now

from video.models import Banner, Video


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
    class Meta:
        model = Video
        # fields = ("author", "id", "cover", "url", "title", "author_name", "view_count", "brief")
        fields = "__all__"
