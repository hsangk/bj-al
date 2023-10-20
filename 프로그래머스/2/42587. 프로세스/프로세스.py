from collections import deque
def solution(priorities, location):
    dic = {}
    for i in range(len(priorities)):
        dic[i]=priorities[i]
    dic2 = list(dic.items())
    # dic2 = sorted(dic.items(), key=lambda x:x[1],reverse=True)
    q = deque()
    result = []
    for i in dic2:
        q.append(i)
    while q:
        x,y = q.popleft()
        y_ = [i[1] for i in q]
        # print(max(y_))
        if len(y_)==0:
            result.append(x)
        else:
            if y >= max(y_):
                result.append(x)
            else:
                q.append((x, y))
        
    answer = 0
    for i in range(len(result)):
        if result[i]==location:
            answer = i+1
    return answer