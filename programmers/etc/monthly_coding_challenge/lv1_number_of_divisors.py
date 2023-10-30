'''
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예

left	right	result
13	    17	    43
24	    27	    52
'''

import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if get_div(i) % 2 == 0: answer += i
        else: answer -= i
    return answer

def get_div(num):
    ret = 0
    for n in range(1,int(math.sqrt(num))+1):
        if num % n == 0:
            ret += 2
        if n*n == num: ret -= 1
    return ret
