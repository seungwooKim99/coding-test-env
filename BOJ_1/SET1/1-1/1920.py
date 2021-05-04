# 1-1. 탐색과 정렬 (1)
# A - 1920 수 찾기
# 2021/05/04


# 시간 초과 코드
"""
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in range(0, len(B)):
    found = False
    for j in range(0, len(A)):
        if A[j] == B[i]:
            print('1')
            found = True
            break
    if not found:
        print('0')
"""

# binary search를 이용한 코드
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def binary_search(start, end, Arr, target):
    while start <= end:
        mid = (start+end)//2
        if Arr[mid] < target:
            start = mid + 1
        elif target < Arr[mid]:
            end = mid - 1
        else:
            return print(1)
    return print(0)

for b in B:
    binary_search(0, N-1, A, b)