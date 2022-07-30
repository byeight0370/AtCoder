V,A,B,C = map(int,input().split())

use_ml = [A,B,C]
result_list = ["F","M","T"]
i = 0
while True:
    V -= use_ml[i]
    if V < 0:
        break
    i += 1
    if i > 2:
        i = 0
print(result_list[i])