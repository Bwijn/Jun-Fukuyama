from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, PermissionDenied, NotAuthenticated, ValidationError
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, fields, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler

from video.models import Video
from rest_framework.response import Response

from .models import Banner

# 视频表 序列化对象
from .serializers import VideoBannerSerializers, VideoSerializers, VideoInfoSerializer


# 首页推荐列表
class VideoView(ReadOnlyModelViewSet):
    permission_classes = []
    queryset = Video.objects.all()
    serializer_class = VideoSerializers
    pagination_class = PageNumberPagination


# 视频详情 API
class VideoDetail(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    queryset = Video.objects.all()
    serializer_class = VideoInfoSerializer
    permission_classes = [IsAdminUser]

    # 在这里返回的serialzers.data字典里面添加上点赞数
    def retrieve(self, request, pk=None, *args, **kwargs):
        # request.user 对象已经被jwt 认证类给赋值了

        try:
            # 返回查询到的视频
            instance = Video.objects.get(id=pk)
        except Exception as e:
            raise NotFound(detail="video resources notfound")
        serializer = self.get_serializer(instance)

        # 当前用户查询是否点赞
        is_like = instance.viewer.filter(id=request.user.id)

        # 查询点赞数量
        likenum = instance.viewer.count()

        # 在返回字典里面添加点赞数量字段
        dic = serializer.data
        dic['likenum'] = likenum

        # 如果查询到 说明已经点赞了 给前端返回过去
        if is_like:
            dic['is_liked'] = 1
        else:
            dic['is_liked'] = 0

        return Response(dic, status=status.HTTP_200_OK)

    # 给视频点赞
    @action(methods=['post'], detail=True, )
    def likeaction(self, request, pk=None, *args, **kwargs):
        instance = request.user.like_r.filter(id=pk)  # 多对多查询 视频id等于pk
        print(instance)
        if instance:
            # 如果点过赞就不向下执行了 直接返回错误信息
            raise ValidationError("You already liked")

        try:
            # 返回查询到的视频
            vo = Video.objects.get(id=pk)
            request.user.like_r.add(vo)
            request.user.like_r.add(vo)
        except Exception:
            raise NotAuthenticated("video resources notfound")

        return Response(data={"msg": "action success"}, status=status.HTTP_201_CREATED)


# 首页轮播图
class VideoBanner(ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = VideoBannerSerializers
