# 다시 풀 문제
# 외계어 사전
def solution(spell, dic):
    answer = 1
    spell = set(spell)
    for i in dic:
        if spell.issubset(set(i)):
            return answer
    return answer + 1
  
# 다른 풀이
def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2

# 안전지대
def solution(board):
    answer = 0
    n = len(board)
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1:
                for k in range(i-1,i+2) :
                    if k == -1 or k == n :  #지뢰가 위/아래 끝에 있을 때
                        continue
                    for p in range(j-1, j+2) :
                        if p == -1 or p == n:  #지뢰가 왼/오 끝에 있을 때
                            continue
                        if board[k][p] != 1 :
                            board[k][p] = 2

    for i in range(n) :
        answer += board[i].count(0)
    return answer
