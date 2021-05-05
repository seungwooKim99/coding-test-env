# 파트 : 1-1. 탐색과 정렬 (1)
# 문제 : B - 2750 수 정렬하기
# 난이도 : 브론즈1
# 푼 날짜 : 2021/05/05

# 파이썬 리스트 내 메소드 이용
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

for i in range(N):
    print(arr[i])