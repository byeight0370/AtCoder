S = input()

for i in range(S):
    if S.count(S[i]) == 1:
        print(S[i])
        break
    if S.count(S[i]) == 2:
        continue
    if S.count(S[i]) == 3:
        print(-1)
        break