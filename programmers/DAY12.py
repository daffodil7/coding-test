# 제곱수 판별
# 내 풀이
import math
def solution(n):
    answer = 0
    if math.sqrt(n)  % 1 == 0:
        answer = 1
    else:
        answer = 2
    return answer
  
# 다른 풀이
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2
