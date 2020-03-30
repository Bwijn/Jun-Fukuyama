from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, PermissionDenied, NotAuthenticated, ValidationError
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, fields, status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework_jwt.utils import jwt_decode_handler
from video.models import Video, Episode
from rest_framework.response import Response

# 视频表 序列化对象
from .serializers import VideoBannerSerializers, VideoList, VideoInfoSerializer, EpisodeDetails


#  排序 推荐 (视频列表) 1.首页推荐列表 2. 分类排序页
class VideoRecommend(ListAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Video.objects.all()
    serializer_class = VideoList
    pagination_class = PageNumberPagination

    def get_queryset(self, sort):
        return Video.objects.all().order_by(sort)

    def get(self, request, *args, **kwargs):
        category = request.query_params.get('category')
        sort = request.query_params.get('sort')

        # 按时间排序
        if sort == "time":
            # todo 数据库添加column 更新时间
            print(self.queryset)
            queryset = self.get_queryset('view_count')
            serializer = VideoList(queryset, many=True)
            print(self.queryset)

            return Response(serializer.data)

        # 按热度排序
        queryset = self.get_queryset('-view_count')  # 注意使用`get_queryset()`而不是`self.queryset`
        serializer = VideoList(queryset, many=True)
        # print(self.queryset)
        # print(serializer)

        return Response(serializer.data)
        return self.list(request, *args, **kwargs)


# 视频详情 API  Details Page [分类] [主演] [剧情介绍]
class VideoDetail(GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    """
    api/video
    api/video/1?addition=type
    api/video/1/1 视频播放页
    {
        "id": 1,
        "author": null,
        "url": "http://127.0.0.1:8080/details/1",
        "cover": "http://img1.imgtn.bdimg.com/it/u=1775789743,1975475802&fm=26&gp=0.jpg",
        "brief": "《进击的巨人》（进撃の巨人），是日本漫画家谏山创创作的少年漫画作品，于2009年在讲谈社旗下的漫画杂志《别册少年Magazine》上开始连载。\r\n该作品曾获2011年“这本漫画真厉害！”男性榜第1名、“讲谈社漫画赏少年部门赏”等奖项 。2012年12月正式宣布TV动画化，2013年4月6日，由WIT STUDIO改编的同名电视动画正式开始放送。\r\n截止至2019年12月25日，单行本（含电子版）累计全球发行量突破1亿册。 [1]",
        "title": "进击的巨人第一季",
        "view_count": 0,
        "likenum": 0,
        "is_liked": 0
    }
    """
    queryset = Video.objects.all()
    serializer_class = VideoInfoSerializer
    permission_classes = [IsAuthenticated]

    # 在这里返回的serialzers.data字典里面添加上点赞数
    # 添加type 分类
    def retrieve(self, request, pk=None, *args, **kwargs):

        # request.user 对象已经被jwt 认证类给赋值了
        try:
            # 返回查询到的视频
            instance = Video.objects.get(id=pk)
        except Exception as e:
            raise NotFound(detail="video resources notfound")
        serializer = self.get_serializer(instance)

        # url参数是否查询了分类
        queryset = request.query_params.get('addition')
        if queryset == 'type':
            # 查询改视频分类组装到serializer.data中返回
            pass
            # dic['type'] = type.name
            # return Response(dic, status=status.HTTP_200_OK)

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


# 分集列表
class Episodes(ListAPIView):
    """
        [
            {
                "episode_num": "1",
                "video_obj": 1,
                "name": "二千年後の君へ"
            },
            {
                "episode_num": "2",
                "video_obj": 1,
                "name": "その日"
            }
        ]
    """
    queryset = Video.objects
    serializer_class = EpisodeDetails

    # 返回分集对象
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        obj = Video.objects.get(id=pk)
        # print(obj)
        obj = obj.episodes.all()
        # print(obj)

        # 返回查询出来的Video实例 所对应的episodes的集数
        return obj

    def get(self, request, *args, **kwargs):
        #  Episodes对象的查询集
        queryset = self.get_queryset()  # 注意使用`get_queryset()`而不是`self.queryset`

        serializer = EpisodeDetails(instance=queryset, many=True)

        return Response(serializer.data)


class PlayVideoView(RetrieveAPIView):
    pass


class Player(RetrieveAPIView):
    """
    {
        "url": "播放地址(播放器初始化需要)",
        "cover": "封面地址"
    }
    """
    queryset = Episode.objects
    serializer_class = EpisodeDetails

    # 返回集对象
    def get_queryset(self):
        pk = self.kwargs.get('episode')
        obj = self.queryset.get(id=pk)
        print(obj)

        return obj

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset()
        ret = {
            'url': instance.url,
            'cover': 'none'
        }

        # serializer = self.get_serializer(instance)
        return Response(ret)

    # def get(self, request, *args, **kwargs):
