# def solution(progresses, speeds):
#     answer = [0] * len(progresses)
#     for i in range(len(progresses)):
#         while progresses[i]<100:
#             progresses[i] += speeds[i]
#             answer[i] += 1
#     answer2 = [0]*len(answer)
#     for i in range(len(answer)):
#         if i == 0:
#             answer2[i] = answer[i]
#         else:
#             if max(answer[:i])>=answer[i]:
#                 answer2[i] = max(answer[:i])
#             else: 
#                 answer2[i] = answer[i]
#     tmp = list(set(answer2))
#     tmp.sort()
#     tmp2 = []
#     for i in range(len(answer2)):
#         a = answer2.count(answer2[i])
#         tmp2.append(a)
#     answer3 = []
#     for i in tmp2:
#         if i not in answer3:
#             answer3.append(i)
    
#     return answer3

def solution(progresses, speeds):
    answer = []
    while progresses:
        # 각 작업에 대해 개발 진도를 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 배포 가능한 작업 확인
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        # 배포 가능한 작업이 있다면 배포
        if count > 0:
            answer.append(count)

    return answer