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
