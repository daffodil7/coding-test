# 다시 풀 문제
# 자릿수 더하기
def solution(n):
    answer = 0
    for n in str(n):
        answer += int(n)
    return answer
