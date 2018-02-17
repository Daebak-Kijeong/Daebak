##Compare the Triplets
import sys
#s = a if a < b else b if문 한줄로
def solve(a0, a1, a2, b0, b1, b2):
    Alice = (1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0)

    Bob = (1 if a0 < b0 else 0) + (1 if a1 < b1 else 0) + (1 if a2 < b2 else 0)
    return (Alice, Bob)
# Complete this function

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))
#태현님 코드
x=list(zip(input().split(),input().split())) #zip함수는 동일한 개수로 이루어진 자료형을 묶어주는 역할
A=sum(int(a)>int(b)for a,b in x)
B=sum(int(a)<int(b)for a,b in x)
print(A,B)


##A Very Big Sum
import sys

from functools import reduce
def aVeryBigSum(n, ar):
    return reduce(lambda x, y: x + y, ar, 0) #lambda함수= 인자 : 표현식 / list(map(함수, 리스트))
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
#태현님 코드
input()
print(sum(map(int,input().split())))


##Diagonal Difference
#input 3
#11 2 4
#4 5 6
#10 8 -12
import sys
def diagonalDifference(a):
    A = 0
    for i in range(n):
        A += a[i][i]
    B = 0
    for i in range(n):
        B += a[i][n-i-1]
        # A = a[0][0] + a[1][1] + a[2][2]
        # B = a[0][2] + a[1][1] + a[2][0]
    return abs(A-B) #abs는 절대값
    # Complete this function
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)

#태현님 코드
N=int(input())
print(abs(sum(((a//N==a%N)-(a//N+a%N+1==N))*int(b) for a,b in zip(range(N*N),' '.join(input() for i in range(N)).split()))))
#zip함수는 zip(iterable*)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
#list(zip([1, 2, 3], [4, 5, 6])) >>>> [(1, 4), (2, 5), (3, 6)]


##Plus Minus
#input 6
#-4 3 -9 0 4 1
import sys

def plusMinus(arr):
    A = [x for x in arr if x > 0]
    B = [x for x in arr if x < 0]
    C = [x for x in arr if x == 0]

    A2 = round(len(A) / n, 6)
    B2 = round(len(B) / n, 6)
    C2 = round(len(C) / n, 6)

    return ('%.6f' %A2 + "\n" +  '%.6f' %B2 + "\n" + '%.6f' %C2)

    # Complete this function
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(plusMinus(arr))


##staircase
import sys
def staircase(n):
    for i in range(1, n + 1):
        a = print(" " * (n - i) + "#" * i)
    return (a)
    # Complete this function
if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)


##Mini-Max Sum
import sys
def miniMaxSum(arr):
    arr.sort() #arr에 뭐가 들어와도 sorting정렬, 거꾸로 정렬은 sort(reverse=True)
    a = sum(arr) #리스트 인자들의 합
    return print((a - arr[-1]), (a - arr[0]))
    # Complete this function

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)


##birthdayCakeCandles
import sys
def birthdayCakeCandles(n, ar):
    a = ar.count(max(ar)) #itertools모듈
    return a
    # Complete this function
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)


##birthdayCakeCandles
import sys
import itertools
def birthdayCakeCandles(n, ar):
    a = ar.count(max(ar)) #itertools모듈 >>> 각 인자들 반환
    for k,v in itertools.groupby(sorted(ar)):
        print(list(v))
    return a
    # Complete this function
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)


##TimeConversion
#input 07:05:45PM
import sys
from time import strptime, strftime
def timeConversion(s):
    a = strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p")) #날짜/시간 형식의 문자열(str)을 datetime형태로 만들려면 strptime을 이용
    #strptime %p >>> Locale’s equivalent of either AM or PM
    #%I >>> Hour (12-hour clock) as a zero-padded decimal number.
    #%H >>> Hour (24-hour clock) as a zero-padded decimal number.
    # from time import localtime, strftime
    # print(localtime())
    # print(type(localtime))
    # strftime("%Y:%m:%d %H:%M:%S", localtime())
    return a
s = input().strip()
result = timeConversion(s)
print(result)


##grading
#4
#73
#67
#38
#33
import sys

def solve(grades):
    result = []
    for i in grades:
        if i >= 38: #Rule4: below 38, the grade will not be modified
            if i % 5 >= 3: #%는 나눈 나머지
               i += (5 - (i % 5))
        result.append(i)

    return result
    # print(grades[1]) if 70 - grades[1] < 3 else print("70")
    # print(grades[2]) if 40 - grades[2] < 3 else print("40")
    # print(grades[3]) if 35 - grades[3] < 3 else print("35")

    # Complete this function
n = int(input().strip())
grades = []
# grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))


##apple-and-orange
#7 11
#5 15
#3 2
#-2 2 1
#5 -6
import sys

def appleAndOrange(s, t, a, b, apple, orange):
    result_A = []
    result_B = []
    for i in apple:
        if (i + a) >= s and (i + a) <= t:
            result_A.append(i)
    for j in orange:
        if (j + b) >= s and (j + b) <= t:
            result_B.append(j)
    result = (len(result_A), len(result_B))
    return result
    # Complete this function

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))


##kangaroo
#input 0 3 4 2
#21 6 47 3
#2081 8403 9107 8400
#x1, x2 <= 10000
import sys

def kangaroo(x1, v1, x2, v2):
    a, b = x1, x2
    if (x1 < x2 and v1 > v2):
        try:
            for i in range(5000):
                for j in range(5000):
                    x1, x2 = a + i*v1, b + j*v2
                    if i == j and x1 == x2:
                        return "YES"
                    else:
                        pass

            else:
                return "NO"
        except:
            return "NO"

    else:
        return "NO"
# Complete this function
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

##태현님 코드
# x+vt=y+wt
# x-y=(w-v)t
x,v,y,w=map(int,input().split())

a=x-y
b=w-v
print(['NO','YES'][a==0 or (b!=0 and a%b==0 and a*b>0)])


##between-two-sets
'''
input
2 3 =  a의 원소의 개수, b의 원소의 개수
2 4 = a의 원소
16 32 96 = b의 원소
<조건>
- x는 a 원소들의 공배수
- x는 b 원소들의 공약수
- 이러한 x 전부의 개수를 output으로 반환
- 2와 4의 공배수는 [4, 8, 12, 16]
- 16, 32, 96의 공약수는 [1, 2, 4, 8, 16]
- 두 리스트의 교집합은 [4, 8, 16]

'''
'''
input
2 3 =  a의 원소의 개수, b의 원소의 개수
2 4 = a의 원소
16 32 96 = b의 원소
<조건>
- x는 a 원소들의 공배수
- x는 b 원소들의 공약수
- 이러한 x 전부의 개수를 output으로 반환
- 2와 4의 공배수는 [4, 8, 12, 16]
- 16, 32, 96의 공약수는 [1, 2, 4, 8, 16]
- 두 리스트의 교집합은 [4, 8, 16]

'''
import sys

def getTotalX(a, b):
    c = [[i for i in range(1, 101) if i % a[j] == 0] for j in range(len(a))]
    d = list(map(set, c))

    def inter(num, T):
        if num <= 1:
            return T[0]
        else:
            for k in range(num - 1):
                T[k + 1] = T[k] & T[k + 1]
            return T[k + 1]
    inter1 = inter(n, d)
    # 약수구하기
    s2 = []
    for i in range(m):  # i=0,1,2
        s = []
        num = int(b[i] / 2)  # b[0] = 16, num = 8
        s.append(b[i])  # b[0] = 16을 s 리스트의 0번째 insert
        while num >= 1:  # num이 1보다 크면
            if b[i] % num == 0:  # 16 % 8 == 0 이면
                s.append(num)  # s 리스트의 0번째에 8을 넣어라
            num -= 1

        s2.append(s)

    for i in range(len(s2)):
        s2[i] = set(s2[i])

    inter2 = inter(m, s2)
    inter3 = set.intersection(inter1, inter2)

    return len(inter3)
    # Complete this function

if __name__ == "__main__":
    n, m = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)

#태현님 코드
input()
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(sum(all(x%a==0 for a in A) and all(b%x==0 for b in B) for x in range(1, max(A+B)+1)))


##breaking-best-and-worst-records
# n = 9
# score = [10,5,20,20,4,5,2,25,1]
# n = 10
# score = [3,4,21,36,10,28,35,5,24,42]
import sys
def breakingRecords(score):
    li = []
    High = []
    Low = []
    #Highest Score
    for i in range(n):
        li.append(score[i])
        if score[i] == max(li) and score[i] != score[0]:
            High.append(score[i])
        elif score[i] == min(li) and score[i] != score[0]:
            Low.append(score[i])
        else:
            pass
    # print(High)
    # print(Low)
    High = set(High)
    Low = set(Low)

    # print(len(High), len(Low))
    return len(High), len(Low)
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))

#태현님 코드
N=int(input())
s=list(map(int,input().split()))
print(len(set(max(s[:i+1]) for i in range(N)))-1, len(set(min(s[:i+1]) for i in range(N)))-1)


##the-birthday-bar
# n = 5
# s = [1,2,1,3,2]
# d,m = [3,2]
# n = 1
# s = [4]
# d,m = [4,1]
# n = 19
# s = [2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
# d,m = 18,7
import sys
from functools import reduce
def solve(n, s, d, m):
    li2 = []
    li = [s[i:m + i] for i in range(int(n))]
    for j in li:
        # print(j)
        if len(j) >= 1 and len(j) == m and sum(j) == d:
            li2.append(j)

    li2 = list(map(tuple, li2))
    li2 = set(li2)

    return len(li2)
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

#태현님 코드
N=int(input())
s=list(map(int,input().split()))
d,m=map(int,input().split())

print(sum(sum(s[i:i+m])==d for i in range(N-m+1)))


##divisible-sum-pairs
# n, k = 6, 3
# ar = [1, 3, 2, 6, 1, 2]
'''
100 22
43 95 51 55 40 86 65 81 51 20 47 50 65 53 23 78 75 75 47 73 25 27 14 8 26 58 95 28 3 23 48 69 26 3 73 52 34 7 40 33 56 98 71 29 70 71 28 12 18 49 19 25 2 18 15 41 51 42 46 19 98 56 54 98 72 25 16 49 34 99 48 93 64 44 50 91 44 17 63 27 3 65 75 19 68 30 43 37 72 54 82 92 37 52 72 62 3 88 82 71
216
num = "43 95 51 55 40 86 65 81 51 20 47 50 65 53 23 78 75 75 47 73 25 27 14 8 26 58 95 28 3 23 48 69 26 3 73 52 34 7 40 33 56 98 71 29 70 71 28 12 18 49 19 25 2 18 15 41 51 42 46 19 98 56 54 98 72 25 16 49 34 99 48 93 64 44 50 91 44 17 63 27 3 65 75 19 68 30 43 37 72 54 82 92 37 52 72 62 3 88 82 71"
ar = list(map(int, num.split()))
n,k = 100,22
'''
import sys

def divisibleSumPairs(n, k, ar):

    li = []
    i = 0
    for x in range(101):
        for y in range(101):
            try:
                if x < y and (ar[x]+ar[y])%k ==0:
                    # print((ar[x],ar[y]),i)
                    li.append((ar[x], ar[y]))
            except IndexError:
                pass
        i += 1

    return len(li)
    # Complete this function

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)

#태현's 코드
n,k=map(int,input().split())
s=list(map(int,input().split()))
print(sum((s[a]+s[b])%k==0 for a in range(n) for b in range(a+1,n)))


##migratory-birds
# n=6
# ar = [1,4,4,4,5,3]
# n=73966
# ar = list(map(int, ex.split()))
# n = 124992
# ar = list(map(int, ex.split()))
import sys

def migratoryBirds(n, ar):
    set_ar = set(ar)
    list_ar = list(set_ar)
    list_ar2 = [ar.count(i) for i in list_ar]
    # li = list(zip(list_ar,list_ar2))
    dic = {list_ar[i]:list_ar2[i] for i in range(len(list_ar))}
    # print(dic)
    li = []
    for num, countnum in dic.items(): #dictionary에 value값 중 max인 key반환
        if countnum == max(dic.values()):
            li.append(num)

    return min(li)
# Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)

#태현's 코드
from collections import Counter as C
input()
print(C(map(int,input().split())).most_common()[0][0])



##day-of-the-programmer

# 256번째 날이 몇월 몇일 인지 반환해줘야함 13.09.2017
# 2월의 경우 2016년엔 윤달로 29일까지 있다. 윤달은 4년 주기로 온다.
# ...2012, 2016, 2020, 2024...
# 근데 1700~1917년까진 Julian calendar를 사용했다.
# 1919년도부턴 Gregorian calendar를 사용했다.
# 1918년에 바뀌었는데, 바뀔때 1918년 1월 31일 다음날이 1918년 2월 14일이었다.
# 이말은 결국, 1918년의 2월은 14일부터 28일까지 즉, 15일인 것이다.
# 이렇게 되면 1918년도엔 256번째되는 날이 26.09.2018 (8월까지 230일)이다.
# 문제는 Julian calendar은 4의 배수로 생각하면 되는데,
# Gregorian calendar 사용부턴 윤달을 조건1)400으로 나눠떨어지고a
# 조건2)4로 나눠떨어지지만 100으로 나눠떨어지면 윤달이 아니다

import sys

def solve(year):

    odd = [y for y in range(1919,2701) if (y%4 == 0 and y%100 !=0) or y%400 == 0]
    odd2 = [y for y in range(1700,1918) if y%4 == 0]
    odd = sorted(odd + odd2)
    # print(odd)
    if year in odd:
        a = "12.09." + str(year)
    elif year == 1918:
        a = "26.09." + str(year)
    else:
        a = "13.09." + str(year)
    # print(a)
    return a
    # Complete this function

year = int(input().strip())
result = solve(year)
print(result)

# 태현's 코드
y=int(input())
g=44-(y%4==0)+(y>1917)*((y%100==0)-(y%400==0))+(y==1918)*13
print('%02d.%02d.%d'%(g%31,8+(g//31),y))



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


#태현's 코드
n,k=map(int,input().split())
cs=list(map(int,input().split()))
bc=int(input())
ba=(sum(cs)-cs[k])/2
print(['%g'%(bc-ba),'Bon Appetit'][bc==ba])




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


##태현's 코드
from collections import Counter as C
input()
print(sum(x//2 for x in C(input().split()).values()))




##drawing-book
# 책은 n page까지 있다.
# 책은 무조건 1장씩 넘긴다.
# 선생님은 p page를 펴라고 했다.
# 항상 시작은 1page에서 시작한다.
# output은 1page가 보이는 부분에서 몇 장을 넘기냐이다.
# n = 6
# p = 2

import sys

def solve(n, p):

    li = [j for j in range(n+2)]
    li2 = []

    try:
        for i in range(0, len(li), 2):
            # print(i)
            li2.append([li[i], li[i + 1]])
            # print(li2)

    except IndexError:
        pass

    li3 = sorted(li2, reverse=True)
    # 책을 1page에서 부터 시작하면
    i = 0
    for a in li2:
        if p in a:
            start = i
        i += 1
    # 책을 마지막page 부터 시작하면
    i = 0
    for b in li3:
        if p in b:
            end = i
        i += 1

    return min(start, end)
# Complete this function

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)


# 태현's 코드
n,p=map(int,[input(),input()])
m=n//2
q=p//2
print(min(q,m-q))


##counting-valleys
#개리는 자전거를 탄다.
#sea level이라 불리는 것은 시작 높이다.
#시작 높이보다 올라갔다 다시 시작 높이까지 내려온 것을 1개의 mountain이라 한다.
#시작 높이보다 내려갔다 다시 시작 높이까지 올라온 것을 1개의 valley라 한다.
#자전거로 n번을 간다.
#올라가는 U 을 +1, D를 -1이라 생각해보면 0에서 시작해서 다시 0으로 돌아오는 것을 생각해보면 될 것 같다.
#output은 valley를 몇 번 했냐는 것 이므로 마이너스가 되었다가 다시 0이 되는 횟수를 반환하면 된다.
# n = 8
# s = "UDDDUDUU"

import sys

def countingValleys(n, s):

    li = []
    num = 0
    for i in s:
        if i == "U":
            num += 1
            li.append(num)
        elif i == "D":
            num -= 1
            li.append(num)
        # print(li)

    count = 0
    for i in range(len(li)):
        if li[i] < 0 and li[i+1] == 0:
            count += 1
            # print(count)

    return count
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)



# 태현's 코드





##electronics-shop
#모니카에겐 s만큼의 돈이 있다. 1<= s <=10^6
#키보드의 종류는 n개다. 1<= n <= 1000
#드라이브의 종류는 m개다. 1<= m <= 1000
#키보드와 드라이브를 하나씩 살 껀데, 수중에 있는 돈의 범위 내에서 최대 가격으로 맞출꺼다.
#만약 키보드나 드라이브 중 하나라도 못 산다면 -1을 프린트
s,n,m = 10,2,3
keyboards = [3,1]
drives = [5,2,8]

import sys

def getMoneySpent(keyboards, drives, s):
    li = [(k+d) for k in keyboards for d in drives]

    li2 = []
    try:
        for v in li:
            if v <= s:
               li2.append(v)

        # print(max(li2))
        return max(li2)
    except:
        # print("-1")
        return "-1"


    # Complete this function

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)


#태현's 코드
from collections import Counter as C
c=C()
input()
print(sum(c.update(x) or c['D']==c['U'] and x=='U' for x in input()))



##cats-and-a-mouse
#x축에 고양이A와 고양이B, 쥐C가 있다.
#x는 고양이A의 위치, y는 고양이B의 위치, z는 쥐C의 위치다.
# q = 3
# x,y,z = 1, 2, 3
# # x,y,z = 1, 3, 2
# # x,y,z = 2, 1, 3
# q = 4
# x,y,z = 1, 4, 2
# q = 5
# x,y,z = 1, 5, 3

import sys

def catAndMouse(x, y, z):
    if abs(z - x) < abs(z - y):
        # print("Cat A")
        return("Cat A")
    elif abs(z - x) > abs(z - y):
        # print("Cat B")
        return("Cat B")
    elif abs(z - x) == abs(z - y):
        # print("Mouse C")
        return("Mouse C")

    # Complete this function

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print ("".join(map(str, result)))


#태현's 코드





##magic-square-forming
import sys

def formingMagicSquare(s):




    # Complete this function

if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)

