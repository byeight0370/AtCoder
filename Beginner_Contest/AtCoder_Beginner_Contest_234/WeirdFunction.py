t = int(input())

def f(n):
    ans = n**2 + 2*n + 3
    return ans

print(f(f(f(t)+t)+f(f(t))))