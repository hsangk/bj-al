def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i != 0 and arr[i] == answer[-1]:
            continue
        elif i ==0 or arr[i]!=answer[-1]:
            answer.append(arr[i])
    return answer