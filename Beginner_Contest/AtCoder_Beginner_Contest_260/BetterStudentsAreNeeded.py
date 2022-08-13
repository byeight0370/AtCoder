import numpy

N,X,Y,Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_index = numpy.array(A)
A_desc_index = numpy.argsort(A_index)[::-1]
print(A_desc_index)
