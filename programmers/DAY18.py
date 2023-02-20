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

# math.gcd : 최대공약수 구하는 함수임

# 다른 풀이
def solution(a, b):
    return 1 if a/b * 1000 % 1 == 0 else 2

# 겹치는 선분의 길이
# &는 집합의 교집합을, |는 집합의 합집합을 추출
def solution(lines):
    sets = [set(range(min(i), max(i))) for i in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
