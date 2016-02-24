# for 문과 range() 함수 예시 #######################

signals = 'blue', 'yellow', 'red'   		   # 3가지 색에 대한 튜플 생성

for x in range(len(signals)):         		   # range() 함수를 통한 for 문 수행
    print(x, signals[x], len(signals[x]))      # 튜플의 색인, 값, 길이 출력

