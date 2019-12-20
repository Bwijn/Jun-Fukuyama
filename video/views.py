from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, fields, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from video.models import Video
from rest_framework.response import Response

from .models import Banner

# 视频表 序列化对象
from .serializers import VideoBannerSerializers, VideoSerializers, VideoInfoSerializer


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
    def retrieve(self, request, pk=None, *args, **kwargs):
        # todo 加上异常 http://www.iamnancy.top/djangorestframework/Exceptions/#notfound

        try:
            # 返回查询到的视频
            instance = Video.objects.get(id=pk)
        except Exception as e:
            raise NotFound(detail="video resources notfound")
        serializer = self.get_serializer(instance)

        # 查询点赞数量
        likenum = instance.viewer.count()

        # 在返回字典里面添加点赞数量字段
        dic = serializer.data
        dic['likenum'] = likenum

        # print(request.query_params, request.user.nickname, request.method, args, kwargs.get('pk'))
        print(dic)
        return Response(dic, status=status.HTTP_200_OK)

    # 给视频点赞
    @action(methods=['post'], detail=True, )
    def likeaction(self, request, pk=None, *args, **kwargs):
        print(pk)

        vo = Video.objects.get(id=pk)
        request.user.like_r.add(vo)
        return Response(data="IIIIIIOP", status=status.HTTP_201_CREATED)


# 首页轮播图
class VideoBanner(ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = VideoBannerSerializers
