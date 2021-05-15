# 파트 : 1-2. 기초 자료구조 (1)
# 문제 : C - 10866 덱
# 난이도 : 실버4
# 푼 날짜 : 2021/05/14

from collections import deque
import sys

queue = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'push_front':
        queue.appendleft(command[1])
    elif command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'pop_front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue.popleft())
    elif command[0] == 'pop_back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue.pop())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        print(1 if len(queue) == 0 else 0)
    elif command[0] == 'front':
        print(-1 if len(queue) == 0 else queue[0])
    else:
        print(-1 if len(queue) == 0 else queue[-1])