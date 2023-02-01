# 다시 풀 문제
# 숨어있는 숫자의 덧셈
import re
def solution(my_string):
    answer = re.findall(r"[0-9]+",my_string)
    result = 0
    for i in answer:
        result += int(i)
    return result

# 다른 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
