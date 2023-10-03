from heapq import heappop, heappush

def solution(book_time):
    for i in range(len(book_time)):
        for j in range(len(book_time[i])):
            hour = book_time[i][j].split(":")[0]
            min = book_time[i][j].split(":")[1]
            book_time[i][j] = int(hour)*60 + int(min)
    print(book_time) 
    book_time.sort()
    answer = 1
    heap = []
    for i,j in book_time:
        if not heap:
            heappush(heap,j)
            continue
        if heap[0] <= i:
            heappop(heap)
        else:
            answer+=1
        heappush(heap, j+10)
                
   
    return answer