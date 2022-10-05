# split
# join
#splitlines

ss = 'Python을 열심히 공부 중'
print(ss.split())
ss = '하나:둘:셋'
print(ss.split(':'))
ss = '하나\n둘\n셋'
print(ss.splitlines())
ss = '%'
print(ss.join('파이썬'))

#출력
'''
['Python을', '열심히', '공부', '중']
['하나', '둘', '셋']
['하나', '둘', '셋']
파%이%썬
'''


#함수 이름 대입

before = ['2022', '12', '31']
after = list(map(int, before))
print(after)