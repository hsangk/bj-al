
def solution(files):
    print(files)
    answer = []
    num = []
    new_files = files.copy()
    for i in range(len(new_files)):
        new_files[i] = list(new_files[i])
        head_id = 0
        while head_id<len(new_files[i]):
            try:
                int(new_files[i][head_id])
                break
            except:
                head_id += 1
        num_id = head_id
        while num_id < len(new_files[i]):
            try:
                int(new_files[i][num_id])
                num_id += 1
            except:
                break
        num.append([files[i][:head_id],files[i][head_id:num_id],files[i]])
        
    num = sorted(num, key=lambda x:(x[0].lower(), int(x[1])))
    num = [x[2] for x in num]
    return num

