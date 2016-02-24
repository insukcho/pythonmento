# pass 문 예시 #######################

signals = 'blue', 'yellow', 'red'            # 3가지 색에 대한 튜플 생성

for x in range(len(signals)):         		    # range() 함수를 통한 for 문 수행
    print(x, signals[x], '루프 시작!')      	# 튜플의 색인, 값, 루프 시작 메시지 출력 
    if signals[x] == 'yellow':
        pass                                    # 아무 작업 하지 않기 
    print(x, signals[x], '루프 종료!!')      	 # 튜플의 색인, 값, 루프 종료 메시지 출력
    
print('프로그램 종료!!')                       # 프로그램 종료 메시지 출력
