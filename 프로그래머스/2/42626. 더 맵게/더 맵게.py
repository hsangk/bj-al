
# from heapq import heappush, heappop

# def solution(scoville, K):
#     heap = scoville.copy()
#     answer = 0 
    
#     while True:
#         a = heappop(heap)
#         if a >= K:
#             break
#         if not heap:
#             answer = -1
#             break
#         b = heappop(heap)
#         sum_ = a + (b*2) 
#         answer += 1
#         heappush(heap, sum_)    
        
    
#     return answer

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    heapify(scoville)  # scoville 리스트를 최소 힙으로 변환
    answer = 0 
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        a = heappop(scoville)
        b = heappop(scoville)
        new_scoville = a + (b * 2)
        heappush(scoville, new_scoville)
        answer += 1
    
    return answer