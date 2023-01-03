# 다시 풀 문제

# 배열 자르기
# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

# 외계행성 나이
# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성
def solution(age):
    answer = ''
    return answer.join([chr(int(i)+97) for i in str(age)])

# 방법2
def solution(age):
    conv = {'0':'a','1':'b','2':'c','3':'d','4':'e'
            ,'5':'f','6':'g','7':'h','8':'i','9':'j'}
    return ''.join(conv[i] for i in str(age))


# 진료 순서 정하기
# 방법1
def solution(emergency):
    answer = sorted(emergency, reverse=True)
    dict = {num:index for index, num in enumerate((answer),start=1)}
    return [dict[num] for num in emergency]

# 방법2
def solution(emergency):
    sort = sorted(emergency, reverse=True)
    return [sort.index(i) + 1 for i in emergency]
