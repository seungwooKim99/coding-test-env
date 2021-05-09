# 파트 : 1-2. 기초 자료구조 (1)
# 문제 : A - 10828 스택
# 난이도 : 실버4
# 푼 날짜 : 2021/05/10

stack = []
N = int(input())
for _ in range(N):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    else:
        print(-1 if len(stack) == 0 else stack[-1])