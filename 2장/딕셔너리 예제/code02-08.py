singer = {} #빈 딕셔너리 생성

#쌍을 만들어 딕셔너리에 추가
singer['이름'] = '트와이스'
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

# 모든 키와 값 출력
for k in singer.keys():
    print("%s --> %s" % (k, singer[k]))