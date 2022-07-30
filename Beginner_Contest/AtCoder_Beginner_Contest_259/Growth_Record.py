N,M,X,T,D = list(map(int,input().split()))

if M >= X:
    print(T)
else:
    X -= M
    print(T - X * D)