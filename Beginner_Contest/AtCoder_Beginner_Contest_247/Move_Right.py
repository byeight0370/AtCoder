S = input()

result = ""
before_number = 0
for s in S:
    s = int(s)
    tmp_number = s
    if not s == 0:
        s -= 1
    result = result+str(s + before_number)
    before_number = tmp_number
print(result)