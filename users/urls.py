from django.urls import path

from . import views

urlpatterns = [
    #   http://localhost:8000/api/auth/login
    path('login', views.Login.as_view()),

    #   http://localhost:8000/api/auth/register
    path('register', views.Register.as_view()),
]
