# 파트 : 1-2. 기초 자료구조 (1)
# 문제 : D - 1406 에디터
# 난이도 : 실버3
# 푼 날짜 : 2021/05/14

from collections import deque
import sys

arr = list(sys.stdin.readline())
arr.pop()
string = deque(arr)
# string = deque(list(map(str, input().split())))
# N = int(sys.stdin.readline())
N = int(sys.stdin.readline())
cursor = len(string)
print(arr)
for _ in range(N):
    # command = list(map(str, sys.stdin.readline().split()))
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor != len(string):
            cursor += 1
    elif command[0] == 'B':
        if cursor != 0:
            del string[cursor - 1]
            cursor -= 1
    else:
        string.insert(cursor, command[1])
        cursor += 1
print(''.join(string))