# 다시 풀어 볼 문제
# 문자열 정렬하기(1)
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isnumeric():
            answer.append(int(i))
            answer.sort()
    return answer
  

# 소인수분해
# 내 풀이
def solution(n):
    answer = []
    for i in range(2,n+1):
        if n%i == 0:
            answer.append(i)

    for i in answer:
        for j in range(2,10000):
            if i*j in answer:
                answer.remove(i*j)
    return answer
  
  # 다른 풀이
  def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
