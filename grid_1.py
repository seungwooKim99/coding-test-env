N, K = map(int, input().split())

result = 0
while True:
    if(N == 1):
        break
    if(N % K != 0):
        result += 1
        N -= 1
    else:
        result += 1
        N /= K

print(result)
