from django.urls import path

from . import views

urlpatterns = [
    # http://localhost:8000/api/video?page=2    查询参数分页加载
    path('video', views.VideoView.as_view(), name="video"),

    # http://localhost:8000/api/video/<int>
    path('video/<int:pk>', views.Video_detail.as_view(), name="video")
]
