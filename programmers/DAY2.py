# 다시 풀어볼 문제

# 최빈값 구하기
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
def solution(array):
    keys = set(array)
    dict = {}
    max_freq = []
    
    for key in keys:
        dict[key] = array.count(key)
        
    for key in keys:
        if dict[key] == max(dict.values()):
            max_freq.append(key)
            
    if len(max_freq) > 1:
        answer = -1
    else:
        answer = max_freq[0]
        
    return answer
  
# ---------------------------------------------------------------------------------------------------------------------------------------------
  
# 피자 나눠먹기(3)
# 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, n명의 사람이 최소 한 조각 이상 피자를 먹으려면 
# 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
import math
def solution(slice, n):
   answer = n / slice 
   return math.ceil(answer)
