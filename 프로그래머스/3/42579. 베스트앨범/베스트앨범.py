from collections import defaultdict

def solution(genres, plays):
    answer = defaultdict(list)
    result = []

    for i in range(len(genres)):
        if len(answer[genres[i]]) > 0:
            answer[genres[i]][0] += plays[i]
            answer[genres[i]][1].append((i,  plays[i]))      
        else:
            time = plays[i]
            songs = [(i, plays[i])]
            answer[genres[i]] = [time,  songs]
    answer = sorted(answer.items(), key=lambda x: -x[1][0])
    # print(answer[0][1])
    for g, (total, idx) in answer:
        # print(answer)
        cnt = 0 
        idx.sort(key = lambda x:x[1], reverse=True)
        print(idx[0][0])
        if len(idx)>=2:
            result.append(idx[0][0])
            result.append(idx[1][0])
        elif len(idx)==1:
            result.append(idx[0][0])
        else:
            continue

    return result