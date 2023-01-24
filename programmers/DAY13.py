# 다시 풀 문제
# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer
  
# 간단풀이
def solution(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]
