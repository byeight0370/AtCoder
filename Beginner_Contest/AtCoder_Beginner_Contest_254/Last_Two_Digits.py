N = input()

count = 0
result = ""
for n in N:
    if count >= 1:
        result += n
    count += 1
print(result)