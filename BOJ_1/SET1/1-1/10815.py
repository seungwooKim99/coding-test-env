# 파트 : 1-1. 탐색과 정렬 (1)
# 문제 : E - 10815 숫자 카드
# 난이도 : 실버4
# 푼 날짜 : 2021/05/05 

def binary_search(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return "1"
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "0"

N = int(input())
Cards = list(map(int, input().split()))
M = int(input())
Compare = list(map(int, input().split()))

Cards.sort()
result = []
for target in Compare:
    result.append(binary_search(0, N-1, Cards, target))

print(' '.join(result))