s = input('영어 대소문자로 이루어진 문장을 입력하세요.\n')  # 문자열 입력

print('모두 대문자로 출력\n' + s.upper())   # 대문자로 모두 변환

print('모두 소문자로 출력\n' + s.lower())   # 소문자로 모두 변환

new_s = str()   # 신규 문자열 형 변수 선언

for c in s:     # 입력 받은 문자를 하나씩 꺼내서 c에 대입

    if c.islower():         # 해당 문자가 소문자이면
        new_s += c.upper()  # 대문자로 변경하여 new_s에 붙이기
    else:                   # 해당 문자가 대문자이면
        new_s += c.lower()  # 소문자로 변경하여 new_s에 붙이

print('대소문자 바꿔서 출력\n' + new_s)             # 최종 변환 결과 출력

print('대소문자 바꿔서 출력\n' + s.swapcase())      # 대소문자 모두 변환
