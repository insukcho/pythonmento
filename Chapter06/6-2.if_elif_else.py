# if - elif - else 문 예시 ##################################

signal_color = input('색을 영문으로 입력하세요: ')     # 색 입력 요청

if signal_color == 'blue':                              # 파란색인 경우
    print('신호등은 파란색입니다. 건너세요.')
elif signal_color == 'red':                             # 빨간색인 경우
    print('신호등은 빨간색입니다. 기다리세요.')
else:                                                   # 모르는 색인 경우
    print('잘못된 색입니다.')
