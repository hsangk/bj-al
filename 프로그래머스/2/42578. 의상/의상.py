def solution(clothes):
    answer = 1
    tmp_d = {}
    for k,v in clothes:
        if v in tmp_d:
            tmp_d[v].append(k)
        else:
            tmp_d[v] = [k]
        
    for k,v in tmp_d.items():
        answer *= (len(v)+1)
    
    return answer-1

