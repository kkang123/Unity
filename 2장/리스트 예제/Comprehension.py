numList = [num for num in range(1, 6)]
print(numList)

# 리스트 = [수식 for 항목 in range() if 조건식]

numList1 = [num * num for num in range(1, 6)]
print(numList1)


numList2 = [num for num in range(1, 21) if num % 3 == 0]
print(numList2)

#2차 컴프리헨션
list2 = [[0 for _ in range(4)] for _ in range(3)]
print(list2)