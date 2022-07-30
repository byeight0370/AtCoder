H,W = list(map(int, input().split()))
R,C = list(map(int, input().split()))

squares = []
count = 0
for h in range(1,H+1):
    for w in range(1,W+1):
        squares.append([h,w])
        if abs(R-h)+abs(C-w)==1:
            count += 1
print(count)