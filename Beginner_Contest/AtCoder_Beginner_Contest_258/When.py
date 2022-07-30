K = int(input())

if K < 60:
    if len(str(K)) == 1:
        print("21:0%d" %(K))
    else:
        print("21:%d" %(K))
else:
    if len(str(K-60)) == 1:
        print("22:0%d" %(K-60))
    else:
        print("22:%d" %(K-60))