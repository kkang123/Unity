ss = "자료구조 & 알고리즘"
print(ss[0])
print('띄어쓰기 있는 문자열리스트 = %s' % ss[1:5])
print(ss[4:])

ss1 = "자료구조& 알고리즘"
print('띄어쓰기 없는 문자열리스트 = %s' % ss1[1:5])
#뛰어쓰기도 문자열의 하나로 봄


ss = '파이썬' + '최고'
print(ss)
ss = '파이썬' * 3
print(ss)

ss = '파이썬abcd'
print(len(ss))

print('-----------------')

ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'
print(ss.count('공부'))
print(ss.find('공부'), ss.rfind('공부'), ss.find('공부', 5), ss.find('없다'))
print(ss.index('공부'), ss.rindex('공부'), ss.index('공부', 5))
print(ss.startswith('파이썬'), ss.startswith('파이썬', 10), ss.endswith('^^'))