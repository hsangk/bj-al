# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)):
#         tmp_list = phone_book[i+1:]
#         for j in phone_book[i+1:]:
#             if phone_book[i] in j:
#                 answer = False
#                 break
#             else:
#                 continue
    
    
#     return answer

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # for j in phone_book[i+1:]:
        # print(phone_book[i+1][0:1])
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
        else:
            continue
    
    
    return answer