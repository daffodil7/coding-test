# 다시 풀어 볼 문제
# 주사위의 개수
def solution(box, n):
    a = box[0]//n
    b = box[1]//n
    c = box[2]//n
    return a*b*c
  
# 합성수 찾기
# 내 풀이
def solution(n):
    answer = 0
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count += 1
            if count >= 3:
                answer += 1
    return answer

# 다른 사람 풀이
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

# 팩토리얼
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
