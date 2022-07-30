N = input()
a_list = list(map(int, input().split()))

a_list = sorted(a_list, reverse=True)

count = 0
result = 0
for a in a_list:
    if count % 2 == 0:
        result += a
        count += 1
    else:
        result -= a
        count += 1
print(result)