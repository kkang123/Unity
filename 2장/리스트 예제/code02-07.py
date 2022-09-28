list1 = []
list2 = []
value = 1

for i in range(0, 3): #3행
    for k in range(0, 4): #4열
        list1.append(value) #list1에 값이 1인 value 입력
        value += 1 # 1에서 += 1하여 for문에 의해 1, 2 ,3 4까지 입력
    list2.append(list1) #for문 i에 list1 값 입력하여 행 정렬
    list1 = [] #초기화? 없으면 1 2 3 4만 무한 반복

for i in range(0, 3):
    for k in range(0, 4):
        print("%3d" % list2[i][k], end = " ") # 3d는 폭이 3번째인 열에서 시작하여 정렬
    print(" ")