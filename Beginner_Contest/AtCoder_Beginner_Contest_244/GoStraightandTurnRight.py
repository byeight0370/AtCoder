N = int(input())
T = input()

x = 0
y = 0
count = 1
for t in T:
    if t == "S":
        if count == 1:
            x += 1
        elif count == 2:
            y -= 1
        elif count == 3:
            x -= 1
        elif count == 4:
            y += 1
    else:
        count += 1
        if count > 4:
            count = 1
print(x,y)