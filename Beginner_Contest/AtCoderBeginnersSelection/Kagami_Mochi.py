N = int(input())

d_list = []
for n in range(N):
    d_list.append(int(input()))

d_list = set(d_list)
print(len(d_list))