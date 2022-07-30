N,Y = map(int, input().split())

value = N+1
result = ""
for a in range(value):
    for b in range(value - a):
        c = N - a - b
        if 10000*a + 5000*b + 1000*c == Y and a + b + c == N:
            result = str(a) + " " + str(b) + " " + str(c)
            break

result = result if result else "-1 -1 -1"
print(result)