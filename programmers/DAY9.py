# 다시 풀 문제
# 영어가 싫어요
# 내 풀이
def solution(numbers):
    nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for index,nums in enumerate(nums):
        numbers = numbers.replace(nums, str(index))
    return int(numbers)

# 다른 사람 풀이
def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)

# 배열의 유사도
# 내 풀이
def solution(s1, s2):
    answer = 0
    for word in s1:
        if word in s2:
            answer += 1
        else:
            continue
    return answer

# 다른 풀이
def solution(s1, s2):
    return len(set(s1)&set(s2))
