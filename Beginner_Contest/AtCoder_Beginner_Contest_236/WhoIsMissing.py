N = int(input())
count = [0] * (N + 1)
for a in map(int, input().split()):
    count[a] += 1
print(count.index(3))