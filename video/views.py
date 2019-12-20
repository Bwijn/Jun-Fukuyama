from django.http import HttpResponse, JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, fields, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from video.models import Video, LikeShip
from rest_framework.response import Response

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

    # 在这里返回的serialzers.data字典里面添加上点赞数
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # print(instance, serializer.data)
        # 查询的视频主键ID
        VPK = kwargs.get('pk')
        # 查询点赞数量
        likenum = LikeShip.objects.filter(video=VPK).count()
        dic = serializer.data
        dic['likenum'] = likenum

        # print(request.query_params, request.user.nickname, request.method, args, kwargs.get('pk'))
        print(dic)
        return Response(dic, status=status.HTTP_200_OK)


# 首页轮播图
class VideoBanner(ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = VideoBannerSerializers
