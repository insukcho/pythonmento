# 피보나치 수열을 위한 모듈

def fib(n):    			# n 까지의 피보나치 수열을 출력 하는 함수
    a, b = 0, 1
    while b < n:
        print(b, end=' ')	# end 기본 값인 줄 넘기기 대신 공백으로 한 줄에 출력
        a, b = b, a+b
    print()			# 줄 넘기기

def fib2(n): 			# n 까지의 피보나치 수열을 반환 하는  함수
    result = []			# 피보나치 수 저장을 위한 리스트 초기화
    a, b = 0, 1
    while b < n:
        result.append(b)	# 리스트 값 채우기
        a, b = b, a+b
    return result		# 피보나치 수 리스트 반환

if __name__ == "__main__":	# 외부에서 호출 시
    import sys
    fib(int(sys.argv[1]))	# 첫 번째 외부 인자 값을 사용하여 fib 호출
