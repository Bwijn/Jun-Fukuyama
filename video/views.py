from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, fields
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from video.models import Video, LikeShip

from .models import Banner

# 视频表 序列化对象
from .serializers import VideoBannerSerializers, VideoSerializers, VideoInfoSerializer, VideoFavorite


# 首页推荐列表
class VideoView(ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    pagination_class = PageNumberPagination


# 视频详情 API
class VideoDetail(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoInfoSerializer


# 首页轮播图
class VideoBanner(ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = VideoBannerSerializers


# 视频点赞视图集
class Favorite(ModelViewSet):
    queryset = LikeShip.objects.all()
    serializer_class = VideoFavorite
