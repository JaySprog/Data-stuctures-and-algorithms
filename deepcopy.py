import copy

a=[1, 2, 3 , 4, 5]
b=copy.deepcopy(a)
a=b

b.remove(3)
print(b)
print(a)
