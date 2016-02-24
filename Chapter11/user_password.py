# 비밀번호 정합성 체크를 위한 함수
def password_validation_check(pwd):
    """ checking password validation

    Args:
        pwd (str) : password string
        
    Return:
        True or False (boolean) : the result of checking validation
    """
    # 비밀 번호 길이 확인 (6~12)
    if len(pwd) < 6 or len(pwd) > 12:
        print(pwd, '의 길이가 적당하지 않습니다.')
        return False

    # 숫자 혹은 알파벳 유무 확인
    for c in pwd:
        if not c.isnumeric() and not c.isalpha():
            print(pwd, '는 숫자와 영문자로만 구성되지 않았습니다.')
            return False

    # 알파벳 대소문자 확인
    upper = False       # 대문자 포함 유무를 위한 논리형 변수
    lower = False       # 소문자 포함 유무를 위한 논리형 변수

    # 각 문자 확인
    for c in pwd:
        
        # 대문자와 소문자가 모두 있으면 루프 탈출
        if upper and lower:
            break               # for 문 탈출

        # 해당 문자가 영문이면
        if c.isalpha():

            # 아직 대문자가 발결 되지 않은 경우에만
            if not upper:
                upper = c.isupper()     # 대문자 포함 유무 저장

            # 아직 소문자가 발결 되지 않은 경우에만
            if not lower:
                lower = c.islower()     # 소문자 포함 유무 저장

    # 대문자 혹은 소문자가 없는 경우 확인
    if not upper or not lower:
        print(pwd, '는 영문 대문자와 소문자가 함께 존재하지 않습니다.')
        return False

    print(pwd, '는 비밀 번호로 적당합니다!')
    return True

if __name__ == '__main__':                     # 이 파일 직접 실행 시(테스트용)
    password_validation_check('23jke')         # False, 길이 오류
    password_validation_check('432rewvb53')    # False, 대문자 부재
    password_validation_check('2@3jke%')       # False, 기호 포함
    password_validation_check('3k39QLe6o0')    # True
