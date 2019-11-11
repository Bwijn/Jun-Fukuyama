from django.utils.timezone import now
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from video.models import Video


# 视频表 序列化对象
class VideoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("author", "id", "cover", "url")
        depth = 1

    # days_since_joined = serializers.SerializerMethodField()  # 图片保存到 现在的时间
    author = serializers.CharField(source="author.userprofile.avatar")  # 作者头像

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
        ser = VideoInfoSerializer(instance=page_roles, many=True)
        return Response(ser.data)
