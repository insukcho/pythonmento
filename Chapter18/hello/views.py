from django.http import HttpResponse       # 응답 모듈 탑재


def index(request):                         # 초기 화면을 위한 함수 정의
    # 응답 문자열 객체 반환
    return HttpResponse("Hello, world. Let's django!!")
