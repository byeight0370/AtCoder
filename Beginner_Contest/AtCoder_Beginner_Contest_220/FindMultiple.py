A,B,C = map(int, input().split())
n = 1
result = -1
while C*n <= B:
    if A <= C*n <= B:
        result = C*n
        break
    else:
        n += 1
print(result)