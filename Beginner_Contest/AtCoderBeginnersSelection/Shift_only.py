N = input()
A = input().split()
 
count = 0
flag = True
while flag:
    A = [int(item) / 2 for item in A]
    A_element = len(A)
    a = [a for a in A if a.is_integer()]
    a_element = len(a)
    if not A_element == a_element:
        flag = False
    else:
        count += 1
else:
    print(count)
