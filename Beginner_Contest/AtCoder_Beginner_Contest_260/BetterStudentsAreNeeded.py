N, X, Y, Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
 
passed = []
 
rank_and_score = []
for i in range(N):
    rank_and_score.append((i+1, A[i], B[i]))

 
rank_and_score.sort(key=lambda x: (x[1], -x[0]))
for i in range(1, X+1):
    passed.append(rank_and_score[-i][0])
if X > 0:
    rank_and_score = rank_and_score[:-X]

rank_and_score.sort(key=lambda x: (x[2], -x[0]))
for i in range(1, Y+1):
    passed.append(rank_and_score[-i][0])
if Y > 0:
    rank_and_score = rank_and_score[:-Y]

rank_and_score.sort(key=lambda x: (x[1] + x[2], -x[0]))
for i in range(1, Z+1):
    passed.append(rank_and_score[-i][0])
if Z > 0:   
    rank_and_score = rank_and_score[:-Z]

passed.sort()
 
passed = list(map(str, passed))
 
print("\n".join(passed))