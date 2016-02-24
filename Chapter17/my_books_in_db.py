import sqlite3  # SQLite3 탑재


# 테이블 생성용 함수
def create_table():
    conn = sqlite3.connect('my_books.db')  # 데이터베이스 커넥션 생성

    cur = conn.cursor()  # 커서 확보

    # my_books 테이블 생성
    cur.execute('''CREATE TABLE my_books (
                        title text,
                        published_date text,
                        publisher text,
                        pages integer,
                        recommendation integer
                )'''
                )

    conn.commit()       # 데이터베이스 반영

    conn.close()        # 커넥션 닫기

if __name__ == "__main__":		               # 외부에서 호출 시
    create_table()          # 테이블 생성 함수 호출
