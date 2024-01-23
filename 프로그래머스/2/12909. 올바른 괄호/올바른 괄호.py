def solution(s):
    answer = True
    tmp = []
    for i in s:
        if i == '(':
            tmp.append(i)
        else:
            if '(' in tmp:
                tmp.pop()
            else:
                tmp.append(i)
    if len(tmp) != 0:
        answer = False
    

    return answer