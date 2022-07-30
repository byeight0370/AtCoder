N = int(input())
S = str(input())

count = 0
for s in S:
    count += 1
    if count == N:
        print(s)
    