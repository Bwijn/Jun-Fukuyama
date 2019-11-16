from django.utils.timezone import now
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, fields
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet
from video.models import Video


# 视频表 序列化对象
class VideoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # fields = ("author", "id", "cover", "url", "title", "author_name", "view_count", "brief")
        depth = 1
        fields = "__all__"

    days_since_joined = serializers.SerializerMethodField()  # 图片保存到 现在的时间
    author = serializers.CharField(source="author.userprofile.avatar")  # 作者头像
    author_name = serializers.CharField(source="author.userprofile.nickname")

    def get_days_since_joined(self, obj):
        """
        现在的时间 - 创建时间
        :param obj:
        :return:
        """
        return (now() - obj.pub_date).days


class PagerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class VideoView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取所有数据
        roles = Video.objects.all()
        # 创建分页对象
        pg = PageNumberPagination()
        # 获取分页的数据
        page_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)
        # 对数据进行序列化

        ser = VideoInfoSerializer(instance=page_roles, many=True, )
        return Response(ser.data)


class Video_detail(APIView):
    def get(self, request, *args, **kwargs):
        # 根据视频主键取值
        pk = kwargs.get("pk")
        # 获取视频单个对象

        video = Video.objects.get(id=pk)
        # 生成单个视频序列化实例

        # 添加了字段 之后序列化
        video_serializer = VideoInfoSerializer(instance=video, many=False, )
        # 返回序列化后的数据
        return Response(video_serializer.data)
