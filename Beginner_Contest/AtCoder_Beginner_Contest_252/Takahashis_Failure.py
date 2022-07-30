N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

max_A = max(A)
count=1
flag = False
for a in A:
    if a == max_A:
        for b in B:
            if count == b:
                flag = True
                break
    count+=1

if flag == False:
    print("No")
else:
    print("Yes")