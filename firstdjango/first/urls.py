from django.urls import path
from . import views  # . -> 현재 위치


urlpatterns = [
    # name : 나중에 front page랑 연동의 편의성을 위해 적어주는 것이 좋다.
    path("", views.home, name="home"),
]
