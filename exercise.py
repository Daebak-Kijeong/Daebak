##sock-merchant
#n개의 양말
#리스트 안의 pair 갯수 찾기
# n = 9
# ex = "10 20 20 10 10 30 50 10 20"
# ar = list(map(int, ex.split()))
# n = 15
# ex = "6 5 2 3 5 2 2 1 1 5 1 3 3 3 5"
# ar = list(map(int, ex.split()))
#output 6
# n = 1
# ar = [100]

import sys
from functools import reduce

def sockMerchant(n, ar):

    se = {}
    for i in range(n):
        se.update({ar[i] : ar.count(ar[i])})
        # print(se)

    even = []
    odd = []
    for j in range(len(se)):
        #pair가 될 수 있는 조건 1보다 큼
        if list(se.values())[j] > 1:

            #pair가 짝수이면 각각의 항목을 2로 나눈 다음 요소를 더하면 됨
            if list(se.values())[j] % 2 == 0:
                even.append(int(list(se.values())[j]/2))
                # print(even)

            #홀수이면 각각의 항목을 1을 먼저 빼고 2로 나눈 다음 요소를 더하면 됨
            elif list(se.values())[j] % 2 == 1:
                odd.append(int((list(se.values())[j]-1)/2))
                # print(odd)

    num = even + odd

    if num == []:
        return 0
    else:
        return reduce(lambda x,y : x+y ,num)

# Complete this function
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)










