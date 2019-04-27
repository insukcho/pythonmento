from django.urls import path        # path 모듈 탑재
from . import views                 # views 모듈 탑재

# url 패턴 추가
urlpatterns = [
    path('', views.show_count, name='show_count'),
]
