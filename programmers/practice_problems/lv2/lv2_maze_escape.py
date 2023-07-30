'''
문제 설명
1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다. 각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다. 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다. 레버 또한 통로들 중 한 칸에 있습니다. 따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다. 이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다. 미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.

미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요. 만약, 탈출할 수 없다면 -1을 return 해주세요.

제한사항
5 ≤ maps의 길이 ≤ 100
5 ≤ maps[i]의 길이 ≤ 100
maps[i]는 다음 5개의 문자들로만 이루어져 있습니다.
S : 시작 지점
E : 출구
L : 레버
O : 통로
X : 벽
시작 지점과 출구, 레버는 항상 다른 곳에 존재하며 한 개씩만 존재합니다.
출구는 레버가 당겨지지 않아도 지나갈 수 있으며, 모든 통로, 출구, 레버, 시작점은 여러 번 지나갈 수 있습니다.

입출력 예
maps	                                    result
["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]	16
["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	-1
'''

from collections import deque

def solution(maps):
    start = get_start(maps)
    lever, count1 = bfs(maps, start, 'L')
    _, count2 = bfs(maps, lever, 'E')
    
    if count1 == -1 or count2 == -1:
        return -1
    return count1 + count2

def get_start(maps):
    for i in range(len(maps[0])):
        for j in range(len(maps)):
            if maps[j][i] == 'S':
                return (i,j)

def bfs(maps, start, target):
    queue = deque([(start, 0)])
    moves = [(0,1), (0,-1), (1,0), (-1,0)]
    history = [[False for i in range(len(maps[0]))] for j in range(len(maps))]
    
    while queue:
        current, count = queue.popleft()
        if maps[current[1]][current[0]] == target: return current, count
        for move in moves:
            next = (current[0]+move[0], current[1]+move[1])
            if 0 <= next[0] < len(maps[0]) and 0 <= next[1] < len(maps):
                if maps[next[1]][next[0]] != 'X' and not history[next[1]][next[0]]:
                    history[next[1]][next[0]] = True
                    queue.append((next, count+1))
    return (0,0), -1
