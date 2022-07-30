N = int(input())

A = list(map(int,input().split()))

B = list(map(int,input().split()))

exist_count = 0
exist_list = []
for a in A:
    b = B.count(a)
    if b >= 1:
        exist_count += 1
        exist_list.append(a)

match_count = 0
for e in exist_list:
    j = B.index(e)
    i = A.index(e)
    if i == j:
        match_count += 1
        exist_count -= 1
print(match_count,exist_count)