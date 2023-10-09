
def solution(people, limit):
    people.sort()
    tmp = [0,len(people)-1]
    answer = 0 
    while tmp[0]<=tmp[1]:
        nx = people[tmp[0]] + people[tmp[1]]
        if nx<=limit:
            tmp[0] += 1
        tmp[1] -= 1
        answer += 1 
    
    return answer