N=int(input())
ST=[[st for st in input().split()] for _ in range(N)]
 
ans="Yes"
for i in range(N):
    flag0=False
    flag1=False
    for j in range(N):
        if i==j:
            continue
        if (ST[i][0] in ST[j]):
            flag0=True
        if (ST[i][1] in ST[j]):
            flag1=True
    if flag0 and flag1:
        ans="No"
        break
print(ans)