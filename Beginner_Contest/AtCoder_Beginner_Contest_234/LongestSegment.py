import math

N = int(input())
coordinate_list = []
for n in range(N):
    coordinate_list.append(list(map(int,input().split())))

len_line_segment_list = []
for coordinate in coordinate_list:
    for coordinate2 in coordinate_list:
        len_line_segment_list.append(math.sqrt((coordinate2[0]-coordinate[0])**2 +(coordinate2[1]-coordinate[1])**2))

print(max(len_line_segment_list))