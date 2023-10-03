from collections import deque

def solution(board):
    a = len(board)
    b = len(board[0])
    print(a, " ", b)
    dx = [-1, 1, 0 , 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    visited = [[False]*b for _ in range(a)]
    
    def bfs(x,y):
        deq = deque()
        deq.append((x,y))
        while deq:
            c, d = deq.popleft()
            visited[c][d] = True
            for i in range(8):
                nx = dx[i] + c
                ny = dy[i] + d
                if 0<=nx<a and 0<=ny<b and not visited[nx][ny]:
                    if board[nx][ny]==1:
                        deq.append((nx,ny))
                    else:
                        board[nx][ny] = 2
                        
    for i in range(a):
        for j in range(b):
            if board[i][j]==1:
                bfs(i,j)
            
    print(board)
    
    answer = 0 
    for i in range(a):
        for j in range(b):
            if board[i][j]==0:
                answer += 1
    
    return answer