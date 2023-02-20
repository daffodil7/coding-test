# 다시 풀 문제
# 유한소수 판별하기
from math import gcd
def solution(a, b):
    b //= gcd(a,b)
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2
  
# 다른 풀이
def solution(a, b):
    return 1 if a/b * 1000 % 1 == 0 else 2
