x, y, n = map(int, input().split())
a = n % 3
b = n // 3
 
print(min(x*a + y*b, x*n))