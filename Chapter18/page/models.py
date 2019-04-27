from django.db import models   # 모델 모듈 탑재


class Visit(models.Model):     # Visit 모델 선언
    count = models.IntegerField(default=0)   # 접속 회수 저장 변수 선언
