import sys

deque = []
n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    if 'push_front' in line:
        # deque[0] = int(line.split(' ')[1])
        deque.insert(0, int(line.split(' ')[1]))
    elif 'push_back' in line:
        deque.append(int(line.split(' ')[1]))
    elif 'pop_front' in line:
        if not deque:
            print(-1)
        else:
            print(deque.pop(0))
    elif 'pop_back' in line:
        if not deque:
            print(-1)
        else:
            print(deque.pop(-1))
    elif 'size' in line:
        print(len(deque))
    elif 'empty' in line:
        if not deque:
            print(1)
        else:
            print(0)
    elif 'front' in line:
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif 'back' in line:
        if not deque:
            print(-1)
        else:
            print(deque[-1])