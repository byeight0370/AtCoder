A,B,C,D = list(map(int,input().split()))

if A - C > 0:
    print("Aoki")
elif A - C < 0:
    print("Takahashi")
else:
    if B - D > 0:
        print("Aoki")
    else:
        print("Takahashi")