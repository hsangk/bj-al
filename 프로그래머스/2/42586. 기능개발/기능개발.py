

# def solution(progresses, speeds):
#     answer = []
#     while progresses:
#         # 각 작업에 대해 개발 진도를 업데이트
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]
#         print(progresses)
#         # 배포 가능한 작업 확인
#         count = 0
#         while progresses and progresses[0] >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1

#         # 배포 가능한 작업이 있다면 배포
#         if count > 0:
#             answer.append(count)

#     return answer

def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            print("1")
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
            print("2")
    answer.append(count)
    return answer