def multi(v1, v2):
    ListEx = []
    res1 = v1 + v2
    res2 = v1 - v2
    res3 = v1 * v2
    res4 = v1 / v2
    res5 = v1 // v2
    ListEx.append(res1)
    ListEx.append(res2)
    ListEx.append(res3)
    ListEx.append(res4)
    ListEx.append(res5)
    return ListEx

myList = []
hap, sub, rhq, ahrt, skajwl = 0, 0, 0, 0, 0

myList = multi(100, 20)
hap = myList[0]
sub = myList[1]
rhq = myList[2]
ahrt = myList[3]
skajwl = myList[4]
print("multi()에서 반환한 값 ==> %d, %d, %d, %d, %d" %(hap, sub, rhq, ahrt, skajwl))
