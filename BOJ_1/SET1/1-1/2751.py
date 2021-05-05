# 파트 : 1-1. 탐색과 정렬 (1)
# 문제 : C - 2751 수 정렬하기 2
# 난이도 : 실버5
# 푼 날짜 : 2021/05/05


# 파이썬 리스트 내 메소드 이용 + sys import
import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

for i in range(N):
    print(arr[i])