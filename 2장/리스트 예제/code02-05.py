aa = []  # 빈 리스트 생성
for i in range(0, 4):
    aa.append(0)    
    # 항목이 4개인 리스트 생성, aa = [0, 0, 0, 0]와 동일
hap = 0

for i in range(0, 4): 
    # 여기서 0~3까지 반복하는 것은 출력에서 input 값 반복
    aa[i] = int(input(str(i + 1) + "번째 숫자 : "))  
    # aa[0] = 값 입력, 첨자 i가 0부터 시작하므로 i + 1로 출력 str() 함수가 숫자를 문자로 변환한 후 "번째 숫자 : "와 합쳐서 '1번 째 숫자 :' 등으로 출력함
hap = 0
for i in range(0, 4):
    hap = hap + aa[i] 
    # 8행부터는 반복문을 사용하여 리스트 값을 합쳐준다.

print("합계 ===> %d" % hap)