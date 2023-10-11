def solution(s):
    print(s)
    tmp = list(s)
    
    for i in range(len(tmp)):
        if i==0 and str(tmp[i]):
            tmp[i] = tmp[i].upper()
        elif tmp[i-1]==' ' and str(tmp[i]):
            tmp[i] = tmp[i].upper()
        else:
            tmp[i] = tmp[i].lower()
    print(tmp)       
    answer = ''.join(tmp)
    
    return answer