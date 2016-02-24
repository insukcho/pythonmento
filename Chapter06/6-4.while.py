# while 문 예시 ##################################

signal_color = ''                                              # 변수 선언 및 초기화

while signal_color != 'blue' and signal_color != 'red':     # 반복문 시작

    signal_color = input('색을 영문으로 입력하세요: ')      # 표준 입력문
     
    if signal_color == 'blue':                                # 파란색인 경우
        print('신호등은 파란색입니다. 건너세요.')
    elif signal_color == 'red':                               # 빨간색인 경우
        print('신호등은 빨간색입니다. 기다리세요.')
    else:                                                      # 모르는 색인 경우
        print('잘못된 색입니다. 다시 입력 하세요.')

print('프로그램을 종료합니다.')                              # 반복문 종료 후 출력
