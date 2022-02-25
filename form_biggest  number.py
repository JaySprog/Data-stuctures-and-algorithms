from itertools import permutations

a=['1', '34', '3', '98', '9', '76', '45', '4']
r=8
combo=list(permutations(a, r))
number=[]
for i in combo:
    number.append("".join(i))
print(max(number))
 
