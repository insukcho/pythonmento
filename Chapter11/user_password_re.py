import re     # re 모듈 탑재


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
    if re.findall('[a-zA-Z0-9]+', pwd)[0]  != pwd:
        print(pwd, '는 숫자와 영문자로만 구성되지 않았습니다.')
        return False

    # 알파벳 대소문자 확인
    if len(re.findall('[a-z]', pwd))==0 or len(re.findall('[A-Z]', pwd))==0:
        print(pwd, '는 영문 대문자와 소문자가 함께 존재하지 않습니다.')
        return False

    print(pwd, '는 비밀 번호로 적당합니다!')
    return True

if __name__ == '__main__':                     # 이 파일 직접 실행 시(테스트용)
    password_validation_check('23jke')         # False, 길이 오류
    password_validation_check('432rewvb53')    # False, 대문자 부재
    password_validation_check('2@3jke%')       # False, 기호 포함
    password_validation_check('3k39QLe6o0')    # True
