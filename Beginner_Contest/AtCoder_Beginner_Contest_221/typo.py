S = input()
T = input()

index = 0
result = "No"
if S == T:
    result = "Yes"
for s in range(len(S)-1):
    ComparisonString = S[:index] + S[index+1] + S[index] + S[index+2:]
    index += 1
    if  ComparisonString == T:
        result = "Yes"
        break
print(result)