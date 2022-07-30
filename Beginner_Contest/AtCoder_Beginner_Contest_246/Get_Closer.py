import math

A,B = map(int, input().split())
d2 = A*A + B*B

d = math.sqrt(d2)
print(A/d,B/d)