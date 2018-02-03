##bon-appetit
# n개의 음식을 시킴 (2<= n <= 10^5)
# k번째 음식은 Anna가 알러지 땜에 못먹음 (0<= k <= n)
# 실수로 k번째 음식값을 Brian이 Anna에게 청구함
# 음식의 값 리스트 ar
# output은 Brian이 줘야할 돈
# n,k = 4,1
# ar = [3,10,2,9]
# b = 12

import sys
from functools import reduce

def bonAppetit(n, k, b, ar):

    if b == int(reduce(lambda x,y : x+y, ar) / 2):
        return int(ar[k]/2)
    elif b == int((reduce(lambda x,y : x+y, ar) - int(ar[k]))/2):
        return "Bon Appetit"

    # Complete this function

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)









