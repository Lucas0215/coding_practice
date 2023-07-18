'''
문제 설명
자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

x에 n을 더합니다
x에 2를 곱합니다.
x에 3을 곱합니다.
자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

제한사항
1 ≤ x ≤ y ≤ 1,000,000
1 ≤ n < y

입출력 예
x	y	n	result
10	40	5	2
10	40	30	1
2	5	4	-1
'''

from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    empty = deque([])
    
    history = [False for i in range(max(y+n, y*3))]
    
    while queue != empty:
        current, count = queue.popleft()
        if current == y: return count
        if current > y: continue
        
        successors = [current+n, current*2, current*3]
        for successor in successors:
            if not history[successor]: 
                history[successor] = True
                queue.append((successor, count+1))
    
    return -1
