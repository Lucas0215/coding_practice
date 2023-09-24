'''
문제 설명
올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. )(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호 쌍의 개수 n이 주어질 때, n개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열의 갯수를 반환하는 함수 solution을 완성해 주세요.

제한사항
괄호 쌍의 개수 N : 1 ≤ n ≤ 14, N은 정수

입출력 예
n	result
2	2
3	5
'''

def solution(n):
    answer = 0
    
    queue = [(1,0)]
    while queue:
        o_count, c_count = queue.pop()
        if o_count == n:
            if o_count > c_count:
                queue.append((o_count, c_count+1))
            else:
                answer += 1
        elif o_count - c_count > 0:
            queue.append((o_count+1, c_count))
            queue.append((o_count, c_count+1))
        else:
            queue.append((o_count+1, c_count))
                
    return answer
