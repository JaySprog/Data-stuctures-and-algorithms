a=[-5, -2, 5, 2, 4, 7, 1, 8,-8,9,10,11,7,3,-4,-10,0]
b=[]
c=[]


for i in a:
    if i>0:
        b.append(i)
    if i<0:
        c.append(i)

            
if len(b)>len(c):
    for i in range(len(c)):
        b.insert(2*i+1,c[i])
    print(b)        

if len(c)>len(b):
    for i in range(len(b)):
        c.insert(2*i+1,b[i])
    print(c)   

