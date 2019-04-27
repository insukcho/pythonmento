from django.http import HttpResponse       # 응답 모듈 탑재
from . import models                       # 모델 탑재


def show_count(request):                   # 접속 회수 출력을 위한 함수 정의

    if models.Visit.objects.count() == 0:  # 데이터 최초 입력 유무 확인
        visit = models.Visit()             # 데이터 레코드 추가를 위한 객체 생성
        visit.save()                       # 데이터 레코드 테이블 입력

    last = models.Visit.objects.last()     # 데이터 레코드 조회
    last.count = last.count +1             # count 1 증가
    last.save()                            # 수정 데이터 반영

    # 응답 문자열 객체 반환
    return HttpResponse("Visit count is >> " + str(last.count))
