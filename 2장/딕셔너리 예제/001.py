#딕셔너리 생성
stu1 = {'학번' : 1000, '이름' : '홍길동' , '학과':'컴퓨터학과'}
print(stu1)

#딕셔너리 키 : 값 추가
stu1['연락처'] = '010-0000-1111'
print(stu1)

#키에 있는 값 변경
stu1['학과'] = '학과가 중복으로 인해 이름 변경'
print(stu1)

#딕셔너리 삭제
del(stu1['학과'])
print(stu1)

#딕셔너리 중복 키 처리
stu1 = {'학번' : 1000, '이름' : '홍길동' , '학과':'컴퓨터학과', '학번' : 2000}
print(stu1)

#키로 값에 접근하는 코드
print(stu1['학번'])
print(stu1['이름'])
print(stu1['학과'])

print(stu1.get('이름'))

#딕셔너리 모든 키 반환
print(stu1.keys())

#dict_keys가 보기 싫으면
print(list(stu1.keys()))


#딕셔너리 모든 값 반환
print(stu1.values())
print(list(stu1.values()))

#딕셔너리 안에 키 유무확인
print('이름' in stu1)
print('주소' in stu1)