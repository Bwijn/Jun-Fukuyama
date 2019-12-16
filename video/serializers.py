from rest_framework import serializers

from video.models import Banner


class VideoBannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
