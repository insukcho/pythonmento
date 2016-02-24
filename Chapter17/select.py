import sqlite3  # SQLite3 탑재


# 전체 조회용 함수
def select_all_books():
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보

    cur.execute('SELECT * FROM my_books')       # 조회용 SQL 실행

    print('[1] 전체 데이터 출력하기')
    books = cur.fetchall()                          # 조회한 데이터 불러오기

    for book in books:                              # 데이터 출력하기
        print(book)

    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_all_books()                              # 전체 조회용 함수 호출
    print('=============================================')

# 일부 조회용 함수
def select_some_books(number):
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보

    cur.execute('SELECT * FROM my_books')       # 조회용 SQL 실행

    print('[2] 데이터 일부 출력하기')
    books = cur.fetchmany(number)                   # 조회한 데이터 일부 불러오기

    for book in books:                             # 데이터 출력하기
        print(book)

    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    select_some_books(3)                            # 일부 조회용 함수 호출
    print('=============================================')

# 1개 조회용 함수
def select_one_book():
    conn = sqlite3.connect('my_books.db')        # 데이터베이스 커넥션 생성
    cur = conn.cursor()                            # 커서 확보

    cur.execute('SELECT * FROM my_books')      # 조회용 SQL 실행

    print('[3] 1개 데이터 출력하기')
    print(cur.fetchone())                          # 데이터 한개 출력하기

    conn.close()                                   # 커넥션 닫기

if __name__ == "__main__":		               # 외부에서 호출 시
    select_one_book()                              # 1개 조회용 함수 호출
    print('=============================================')


# 쪽수 많은 책 조회용 함수
def find_big_books():
    conn = sqlite3.connect('my_books.db')         # 데이터베이스 커넥션 생성
    cur = conn.cursor()                             # 커서 확보

    # 조회용 SQL 실행 (300 쪽이 넘는 책의 제목과 쪽수를 출력하라)
    cur.execute('SELECT title, pages FROM my_books WHERE pages > 300')

    print('[4] 페이지 많은 책 출력하기')
    books = cur.fetchall()                          # 조회한 데이터 불러오기

    for book in books:                              # 데이터 출력하기
        print(book)

    conn.close()                                    # 커넥션 닫기

if __name__ == "__main__":		                # 외부에서 호출 시
    find_big_books()                                # 쪽수 많은 책 조회용 함수 호출
    print('=============================================')