# 다시 풀 문제
# 문자열 계산하기(eval)
def solution(my_string):
    answer = 0
    return eval(my_string)

# 다른 방법
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
