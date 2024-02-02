import copy

def solution(n, wires):
    answer = n

    m = {}

    for w in wires:
        if w[0] in m:
            m[w[0]].append(w[1])
        else:
            m[w[0]] = [w[1]]
        if w[1] in m:
            m[w[1]].append(w[0])
        else:
            m[w[1]] = [w[0]]
    print(m)
        
    def getCount(s, m):
        result = 1

        for num in m[s]:
            m[num].remove(s)
            result += getCount(num, m)

        return result

    for i in range(1, n + 1):
        for nn in m[i]:
            new_m = copy.deepcopy(m)
            new_m[i].remove(nn)
            new_m[nn].remove(i)

            tree_diff_count = abs(getCount(i, new_m) - getCount(nn, new_m))
            answer = min(answer, tree_diff_count)

    return answer