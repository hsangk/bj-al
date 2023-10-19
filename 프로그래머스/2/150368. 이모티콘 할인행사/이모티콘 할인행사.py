# from itertools import product
# def solution(users, emoticons):
#     comb = list(product([10,20,30,40], repeat =len(emoticons))
#     print(users)
#     print(emoticons)
#     tmp = list([0,0]*len(comb))
#     for c in comb:
#         for i in range(len(emoticons)):
#             for u in range(len(users)):
#                 if users[u][0] >= c:
#                     result = sum(emoticons*)
        
        
        
    
#     answer = []
#     return answer

                
from itertools import product

def solution(users, emoticons):
    rate = [10, 20, 30, 40] 

    repeat_n = len(emoticons)

    rate_lst = list(product(rate, repeat = repeat_n)) 

    case_lst = [] 
    for rate in rate_lst:
        emo_plus = 0
        emo_purchase = 0

        for user in users:

            customer_rate = user[0]
            customer_price = user[1]

            price_lst = [int(emoticons[i] * (100 - rate[i]) / 100) 
                         for i in range(len(rate))]
            # print(price_lst)
            purchase = []


            for rate_ in rate:
                if rate_ >= customer_rate: 
                    purchase.append(1)
                else:
                    purchase.append(0)


            total_purchase = [purchase[i] * price_lst[i] for i in range(len(price_lst))]

            cond = sum(total_purchase)

            if cond >= customer_price:
                emo_plus += 1
            else:
                emo_purchase += cond

        case_lst.append([emo_plus, emo_purchase])

    
    case_lst.sort(key=lambda x:(x[0],x[1]),reverse=True)
    # print(case_lst)
    
    return case_lst[0]


