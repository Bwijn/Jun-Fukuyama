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
from rest_framework.routers import Route, SimpleRouter
from rest_framework_jwt.views import obtain_jwt_token
from users.views import UserViewset
from video.views import VideoBanner, VideoView, VideoDetail

router = SimpleRouter()
router.register('api/user', UserViewset, base_name='user')  # 只能post创建新用户
router.register("api/homerecommend", VideoView)  # 首页推荐List     http://127.0.0.1:8000/api/homerecommend/
router.register("api/video", VideoDetail)  # 视频详情               http://127.0.0.1:8000/api/video/3

urlpatterns = [
    # 管理员
    path('admin/', admin.site.urls),
    # drf 路由器自动生成url 包括 用户注册
    # 自动生成的路由在上面router.register里面注册
    path('', include(router.urls)),

    # user token 登录 令牌
    # http://127.0.0.1:8000/api-token-auth
    path('api-token-auth', obtain_jwt_token),

]
