import sqlite3                                      # sqlite3 모듈 탑재
from Chapter17.select import select_one_book        # 데이터 조회용 함수 탑재


# 데이터 수정용 함수
def update_books():
    conn = None

    # 업데이트를 위한 try문 선언
    try:

        conn = sqlite3.connect('my_books.db')       # 데이터베이스 커넥션 생성
        cur = conn.cursor()                         # 커서 확보

        # 데이터 수정 SQL ( 제목이 ? 인 책의 추천 유무를 ? 로 변경하라 )
        update_sql = 'UPDATE my_books SET recommendation=? WHERE title=?'

        # 수정 SQL 실행
        cur.execute(update_sql, (2, '클린 코드'))

        conn.commit()                               # 데이터베이스 반영 (커밋)

    # 예외 처리를 위한 except문 선언
    except:

        print ("예외 상황 발생")
        conn.rollback()                          # 데이터베이스 원복 (롤백)

    # 정상 및 예외 처리 후 자원 해제를 위한 finally문 선언
    finally:

        if conn:                                     # 커넥션 확보 유무 확인
            conn.close()                            # 커넥션 닫기

if __name__ == "__main__":		            # 외부에서 호출 시
    select_one_book()
    update_books()                                  # 데이터 수정 함수 호출
    print('[데이터 수정 완료] ================== ')
    select_one_book()
