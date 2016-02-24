from django.conf.urls import url        # url 모듈 탑재
from . import views                     # views 모듈 탑재

# url 패턴 추가
urlpatterns = [
    url(r'^$', views.index),
]
