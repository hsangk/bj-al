
def solution(elements):
    answer = 0
    new_ele = elements*2
    tmp = []
    for i in range(len(elements)):
        for j in range(len(new_ele)-i):
            answer = sum(new_ele[j:j+i+1]) 
            tmp.append(answer)
    # print(tmp)
    result = set(tmp)
    answer2 = len(result)
    return answer2