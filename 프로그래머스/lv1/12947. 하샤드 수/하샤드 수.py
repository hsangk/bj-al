def solution(x):
    answer = True
    sum_ = 0
    for i in list(str(x)):
        sum_ += int(i)
    if x%sum_==0:
        answer = True
    else:
        answer = False
    return answer