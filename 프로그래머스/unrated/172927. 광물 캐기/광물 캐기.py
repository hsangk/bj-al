def solution(picks, minerals):
    answer = 0 
    sum = 0 
    
    for i in picks:
        sum += i 
    
    num = sum * 5
    if len(minerals)> sum : 
        minerals = minerals[:num]
        
    new_mine = [[0]*3 for _ in range(len(minerals)//5+1)]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            new_mine[i//5][0]+=1
        elif minerals[i]=='iron':
            new_mine[i//5][1]+=1
        elif minerals[i]=='stone':
            new_mine[i//5][2]+=1
    
    new_mine.sort(key=lambda x:(-x[0], -x[1], -x[2]))
    
    for i in new_mine:
        a,b,c = i 

        for j in range(len(picks)):
            if picks[j]>0 and j ==0:
                picks[j] -= 1 
                answer += a + b + c
                break
            elif picks[j]>0 and j == 1:
                picks[j] -=1
                answer += 5*a + b + c
                break
            elif picks[j]>0 and j ==2:
                picks[j] -= 1
                answer += 25*a + 5*b + c
                break
            
    
    return answer