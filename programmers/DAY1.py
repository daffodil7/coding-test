# 다시 풀 문제

# 분수의 덧셈
# 첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(denum1, num1, denum2, num2):
    answer = []
    # 두 수가 배수관계일때.
    if max(num1,num2)%min(num1,num2)==0:
        tmp =  max(num1,num2)//min(num1,num2)
        if num1 <=num2:
            answer = [denum1*tmp+denum2, num2]
        else:
            answer = [denum2*tmp+denum1, num1]
    # 두 수가 배수관계가 아닐때.
    else:
        answer = [denum2*num1+denum1*num2, num1*num2]
    
    # 약분되는지 판별
    div = 2
    while min(answer[0],answer[1])>=div:
        if answer[0]%div==0 and answer[1]%div==0:
            answer[0] = answer[0]//div
            answer[1] = answer[1]//div
        else:
            div+=1
    return answer
