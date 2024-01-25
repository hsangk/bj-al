# def solution(number, k):
#     answer = ''
#     print(number)
#     print(k)
#     a = list(number)
#     for i in range(len(a)-k):
    
def solution(number, k):
    answer = []
    for i in number:
        if not answer:
            answer.append(i)
            continue
        # print(number)
        # print(answer)
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)
        