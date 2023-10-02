from collections import deque

def solution(maps):

    answer = 0
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    def bfs(start, end):
        visited = [[0]*b for _ in range(a)]
        visited[start[0]][start[1]] == 0
        queue = deque([start])
        while queue:
            cx, cy = queue.popleft()
            cnt = 0
            cnt2 = cnt 
            for k in range(4):
                    nx = cx + dx[k]
                    ny = cy + dy[k]
                    
                    if 0<=nx<a and 0<=ny<b and maps[nx][ny] != "X" and visited[nx][ny]==0:
                        visited[nx][ny] = visited[cx][cy] + 1
                        # cnt2 = cnt
                        cnt2 += 1
                        queue.append((nx,ny))
                   
        return visited[end[0]][end[1]]

    a = len(maps)
    for i in range(len(maps)):
        maps[i] = list(maps[i])
    b = len(maps[0])
    
    for i in range(a):
        for j in range(b):
            if maps[i][j] == "S":
                st = (i,j)
            elif maps[i][j] == 'L':
                en1 = (i,j)
            elif maps[i][j] == 'E':
                en2 = (i,j)
    # print(st, en1 ,en2)
    time1 = bfs(st,en1)
    time2 = bfs(en1,en2)
    if time1 == 0 or time2 == 0:
        answer = -1
    else:
        answer = time1 + time2
            
    return answer