#global 예약어

#함수 선언
def func1():
    global a # 이 함수 안에서 a는 전역 변수
    a = 10
    print("func1()에서 a 값 %d" % a)

def func2() :
    print("func2()에서 a 값 %d" % a)

#함수 변수 선언 부분
a = 20 #전역 변수

#메인 코드
func1()
func2()

#출력
'''
func1()에서 a 값 10
func2()에서 a 값 10
'''
#global 예약어로 지역 변수인 a를 전역 변수로 지정해준다.