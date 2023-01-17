# 다시 풀 문제
# 가까운 수
# 내 풀이
def solution(array, n):
    array.sort()
    answer = 0
    com = n+100
    for i in array:
        if abs(i-n) < com:
            com = abs(i-n)
            answer = i
    return answer

# 다른 사람 풀이
def solution(array, n):
    array.sort()
    temp = []
    for i in array :
        temp.append( abs(n-i) )

    return array[temp.index(min(temp))]

# 암호해독
# 내 풀이
def solution(cipher, code):
    answer = ''
    for i in range(code,len(cipher)+1):
        if i % code == 0:
            answer += cipher[i-1]
    return answer

# 다른 사람 풀이
def solution(cipher, code):
    return cipher[code-1::code]
