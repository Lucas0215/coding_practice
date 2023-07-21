'''
문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers	return
"17"	3
"011"	2
'''

def solution(numbers):
    numbers = [str(number) for number in numbers]
    primes = set()
    queue = [('', numbers)]
    
    while queue:
        num, num_list = queue.pop()
        for i, n in enumerate(num_list):
            primes.add(int(num+n))
            queue.append((num+n, num_list[:i]+num_list[i+1:]))

    primes = [n for n in primes if is_prime(n)]
    return len(primes)

def is_prime(n):
    if n < 2: return False
    
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0: return False
    return True
