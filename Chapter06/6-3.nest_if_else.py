# 중첩 if 문 예시 ##################################

signal_color = input('색을 영문으로 입력하세요: ')         # 색 입력 요청

if signal_color == 'blue':                                  # 파란색인 경우
    print('신호등은 파란색입니다. 건너세요.')

    is_pass = input('건널 준비가 되었나요? (yes/no)')    # 건널 준비가 되었는지 확인
    if is_pass == 'yes':                                    # 준비가 된 경우
        print('건너겠습니다!!')
    else:                                                   # 준비가 안 된 경우
        print('다음 번에 건너겠습니다.')
    
elif signal_color == 'red':                                 # 빨간색인 경우
    print('신호등은 빨간색입니다. 기다리세요.')
else:                                                       # 모르는 색인 경우
    print('잘못된 색입니다.')
