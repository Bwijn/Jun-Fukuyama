from django.contrib import admin
from .models import Video, VideoName, Episode, Type

# Register your models here.
admin.site.register(Video)
admin.site.register(VideoName)
admin.site.register(Episode)
admin.site.register(Type)
