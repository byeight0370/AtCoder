N = int(input())

A_list = list(map(int,input().split()))

result = 0

flag = True
while flag:
    if A_list.count(result) >= 1:
        result += 1
    else:
        flag = False
print(result)