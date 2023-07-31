import sys

queue = []
n = int(sys.stdin.readline())

for i in range(n):
    line = sys.stdin.readline()
    if "push" in line:
        queue.append(int(line.split(' ')[1]))
    elif "pop" in line:
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif "size" in line:
        print(len(queue))
    elif "empty" in line:
        if not queue:
            print(1)
        else:
            print(0)
    elif "front" in line:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif "back" in line:
        if not queue:
            print(-1)
        else:
            print(queue[-1])
