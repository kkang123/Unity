#반환 값이 여러 개인 함수

#함수 선언
def multi(v1, v2) :
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

#전역 변수 선언
myList = []
hap, sub = 0, 0

#메인 코드
myList = multi(100, 200) #myList 변수에 함수 multi 실행
hap = myList[0] #hap 값을 리스트 0번인 res1에 삽입
sub = myList[1] #sub 값을 리스트 1번인 res2에 삽입
print("multi()에 반환한 값 ==> %d %d" %(hap, sub))

#출력
'''
multi()에 반환한 값 ==> 300 -100
'''