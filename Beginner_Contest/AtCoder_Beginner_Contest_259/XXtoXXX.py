S=input()
T=input()
s=len(S)
t=len(T)
ans='Yes'
j=0
for i in range(t):
  if j==s and T[i]==S[j-1]==S[j-2]:
    continue
  elif j==s:
    ans='No'
    break
  elif T[i]==S[j]:
    j+=1
    continue
  elif T[i]!=S[j] and T[i]==S[j-1]==S[j-2]:
    continue
  ans='No'
  break
print(ans)