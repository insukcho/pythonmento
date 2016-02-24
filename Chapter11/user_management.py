import user_email as ue             # user_email 모듈 탑재
import user_password_re as upr      # user_password_re 모듈 탑재

# 사용자 클래스 정의
class User:
    """ This class keeping user's email address and password

    Put email address & password when creating instance.
    And also need to check validation of address & password.
    """
    # 초기화 함수 재정의
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
        self.check_validation()     # 입력 한 이메일 주소 및 비밀 번호 검증

    # 정합성 검증 함수 호출을 통한 이메일 주소 및 비밀 번호 적합성 검증
    def check_validation(self):
        """checking email & password validation
        """
        ue.email_validation_check(self.email)       # 이메일 정합성 검증
        upr.password_validation_check(self.pwd)     # 비밀번호 정합성 검증

if __name__ == '__main__':                          # 이 파일 직접 실행 시(테스트용)
    user1 = User('isi.cho@gmail.com', '3jkMf8Exe')  # 적합함
    print('=====================================')
    user2 = User('isi.cho@gm@il*c0m', 'eee')        # 적합하지 않음
    print('=====================================')
    user3 = User('i#i.cho@gmail.com', '3#kMEx90e')  # 적합하지 않음
