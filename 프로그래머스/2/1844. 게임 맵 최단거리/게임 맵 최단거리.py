def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    # print(N)
    # print(M)
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    tmp = [[0,0]]
    while tmp:
        x, y = tmp.pop(0)
        visited[x][y] = 1
        # print(x)
        for i in range(len(dx)):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    tmp.append((nx,ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    if visited[-1][-1]:
        answer = maps[-1][-1]
        return answer
    else:
        return -1
    
    return answer