# 파트 : 1-1. 탐색과 정렬 (1)
# 문제 : D - 10989 수 정렬하기 3
# 난이도 : 실버5
# 푼 날짜 : 2021/05/05

import sys

N = int(sys.stdin.readline())

arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)