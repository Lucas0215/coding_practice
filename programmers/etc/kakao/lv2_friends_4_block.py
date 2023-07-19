'''
https://school.programmers.co.kr/learn/courses/30/lessons/17679

문제 설명
프렌즈4블록
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2x2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

board map
만약 판이 위와 같이 주어질 경우, 라이언이 2x2로 배치된 7개 블록과 콘이 2x2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2x2에 포함될 수 있으며, 지워지는 조건에 만족하는 2x2 모양이 여러 개 있다면 한꺼번에 지워진다.

board map

블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

board map

만약 빈 공간을 채운 후에 다시 2x2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
board map

위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

입력 형식
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
출력 형식
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

입출력 예제
m	n	board	                                                        answer
4	5	["CCBDE", "AAADE", "AAABF", "CCBBF"]	                        14
6	6	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	15
'''

infinite = 100

def solution(m, n, board):
    board = [[[i, board[m-i-1][j]] for i in range(m)] for j in range(n)]
    before, answer = -1, 0
    dx, dy = [0,1,0,1], [0,0,1,1]
    
    while before != answer:
        before = answer
        for i in range(n-1):
            for j in range(m-1):
                if board[i][j][1] == board[i+1][j][1] == board[i][j+1][1] == board[i+1][j+1][1]:
                    for k in range(4):
                        if board[i+dx[k]][j+dy[k]][0] != infinite: answer += 1
                        board[i+dx[k]][j+dy[k]][0] = infinite
    
        for i in range(len(board)):
            board[i] = custom_sort(board[i])
    return answer

def custom_sort(array):
    ret_array = []
    count = 0
    for index, char in array:
        if index != infinite:
            ret_array.append([index, char])
        else: count += 1
        
    return ret_array + [[infinite, '-']]*count
