from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.db import DatabaseError
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from users.models import User


# http://localhost:8000/api/auth/login
class Login(APIView):

    def post(self, request):
        print(request.headers)
        formdata = request.data
        # 获取用户名和密码
        username = formdata.get('username')
        password = formdata.get('password')
        # 认证user对象
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            request.session.set_expiry(120)
            avatar = user.userprofile.avatar

            # 将session哈希值传入返回
            session = request.session.get('_auth_user_hash')
            # print(request.session.items())
            ret = {
                'userSession': session,
                'userName': username,
                'avatar': avatar
            }
            return JsonResponse(ret, status=201)

        return JsonResponse({'error': "user", 'detail': '账号或密码错误'}, status=400)


class Register(APIView):
    # def get(self, request):
    #     return JsonResponse({'code': 1})

    # 新建用户 POST
    def post(self, request):
        # 获取用户名和密码 邮箱
        username, password = (request.data.get('username'), request.data.get("password"))
        email = request.data.get("email")
        print(username, password, email)

        # 判断填写是否正确
        if not all([username, password, email]):
            # 400 Bad Request：服务器不理解客户端的请求，未做任何处理。
            return JsonResponse(
                {
                    "error": "Invalid payload.",
                    "detail": {
                        "param": "missing parameters."
                    }
                },
                status=400)

        try:
            user = User.objects.create_user(username=username, email=email, password=password, )
            user.save()
        except DatabaseError:
            return JsonResponse(
                {
                    "error": "DatabaseError",
                    "detail": {
                        "username": "Duplicate Name"
                    }
                },
                status=500)
        return JsonResponse({"code": 000, "MSG": "成功"}, status=201)
