N,A,B=map(int, input().split())

result = 0
for integer in range(N + 1):
    sum_total = sum([int(number) for number in str(integer)])
    if A <= sum_total <= B:
        result += integer
print(result)
