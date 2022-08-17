import math
X, Y = map(int, input().split())

if Y-X < 0:
    print(0)
else:
    print(math.ceil((Y-X) / 10))