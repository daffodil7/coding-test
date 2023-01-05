# 구슬을 나누는 경우의 수
# 나만의 풀이
import math
def solution(balls, share):
    how = balls - share
    b = (math.factorial(how) * math.factorial(share))
    answer = math.factorial(balls) / b
    return answer
  
# 다른 사람 풀이
import math
def solution(balls, share):
    return math.comb(balls, share)
  
# 공 던지기
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]


# 배열 회전시키기
from collections import deque

def solution(numbers, direction):
    num_deque = deque(numbers)
    if direction == 'right':
        num_deque.rotate(1)
    else:
        num_deque.rotate(-1)
    return list(num_deque)
