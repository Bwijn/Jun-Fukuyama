from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, fields
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from video.models import Video

from .models import Banner

# 视频表 序列化对象
from .serializers import VideoBannerSerializers, VideoSerializers, VideoInfoSerializer


# 首页的轮播图API
class VideoView(ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers


# 视频详情 API
class VideoDetail(GenericViewSet, RetrieveModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoInfoSerializer


# 首页轮播图
class VideoBanner(ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = VideoBannerSerializers
