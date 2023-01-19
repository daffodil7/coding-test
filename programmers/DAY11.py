# 다시 풀 문제
# 자릿수 더하기
def solution(n):
    answer = 0
    for n in str(n):
        answer += int(n)
    return answer

# OX 퀴즈
def solution(quiz):
    answer = []
    for i in quiz:
        s = i.split()
        if s[1] == '-':
            if (int(s[0]) - int(s[2])) == int(s[len(s)-1]):
                answer.append('O')
            else:
                answer.append('X')
        if s[1] == '+':
            if (int(s[0]) + int(s[2])) == int(s[len(s)-1]):
                answer.append('O')
            else:
                answer.append('X')
    return answer

# 다른 풀이
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]
