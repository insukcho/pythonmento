import re                                           # re 모듈 탑재

# 이메일 주소 정합성 체크를 위한 함수
def email_validation_check(email):
    """ checking e-mail address validation

    Args:
        email (str) : e-mail address string
        
    Return:
        True or False (boolean) : the result of checking validation
    """
    # 이메일 주소 정합성 유무 확인
    if re.findall(r'[\w.-]+@[\w.-]+.\w+', email)[0]  != email:
        print(email, '는 이메일 주소 형식에 맞지 않습니다.')
        return False

    print(email, '는 이메일 주소로 적당합니다!')
    return True

if __name__ == '__main__':                          # 이 파일 직접 실행 시(테스트용)
    email_validation_check('#@c#o@gmail*om')        # False
    email_validation_check('isi.cho@gmail.com')     # True
    
