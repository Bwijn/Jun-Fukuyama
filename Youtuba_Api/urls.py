"""
Raqo URL配置

urlpatterns列表将URL路由到视图。有关更多信息，请参见：
    https://docs.djangoproject.com/zh-CN/2.2/topics/http/urls/
例子：
功能视图
    1.添加导入：从my_app导入视图
    2.将URL添加到urlpatterns：path（''，views.home，name ='home'）
基于类的视图
    1.添加一个导入：from other_app.views import Home
    2.将URL添加到urlpatterns：path（''，Home.as_view（），name ='home'）
包括另一个URLconf
    1.导入include（）函数：从django.urls导入include，路径
    2.将URL添加到urlpatterns：path（'blog /'，include（'blog.urls'））
"""
from django.contrib import admin
from django.urls import path, include, re_path

# 注册路由器
from rest_framework.routers import Route, SimpleRouter, DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from users.views import UserViewset, avatar_handle
from video.views import VideoBanner, VideoRecommend, VideoDetail, VideoDetailsPage

from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register('api/user', UserViewset, )  # 只能post创建新用户
router.register("api/video", VideoDetail)  # 视频详情               http://127.0.0.1:8000/api/video/3
# router.register("api/details", VideoDetailsPage.as_view())  # # 剧情介绍 分类 分集页

urlpatterns = [
    # 管理员
    path('admin/', admin.site.urls),

    # 可以将 router.urls 附加到现有视图的列表中...
    path('', include(router.urls)),

    # 头像处理 todo 加上userid
    path('api/upload', avatar_handle, name="avatar_upload_handle"),

    # user token 登录 令牌
    # http://127.0.0.1:8000/api-token-auth
    path('api-token-auth', obtain_jwt_token),
    path('api-token-verify', verify_jwt_token),

    # coreapi 自动生成的api文档
    # http://127.0.0.1:8000/api/docs
    path("api/docs/", include_docs_urls(title="API 文档")),

    # 动漫排序 时间 or 热度 ranking?category=anime&sort=hot
    path("api/ranking", VideoRecommend.as_view()),

    # 热门推荐
    path("api/recommend", VideoRecommend.as_view()),

    # 剧集
    path('api/details/<pk>', Episodes.as_view()),

    # 播放页
    path('api/play/video/<videoid>/<episode>', PlayVideoView.as_view()),

    # 初始化播放器
    path('api/player/<videoid>/<episode>', Player.as_view())
]
