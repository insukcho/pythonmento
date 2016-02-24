books = list()      # 책 목록 선언

# 책 목록 만들기
books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12', '출판사':'A', '쪽수':248, '추천유무':True})

many_page = list()                              # 책 리스트 선언
recommends = list()                             # 책 리스트 선언
all_pages = int()                               # 전체 쪽수 변수 선언
pub_companies = set()                           # 출판사 집합 선

for book in books:                              # 책 한 권씩 꺼내기 위한 루프 선언
    if book['쪽수'] > 250:                       # 250쪽 넘는 책 목록 만들기
        many_page.append(book['제목'])
    if book['추천유무']:                          # 책 추천 목록 만들기
        recommends.append(book['제목'])
    all_pages = all_pages + book['쪽수']         # 책 쪽수 더하기
    pub_companies.add(book['출판사'])

print('쪽수가 250 쪽 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_companies)
