def Imultarray (a,n):
    rotated_a=[]
    rotated_a.append(a[n-1])
    
    for i in range (0,n-1):
            rotated_a.append(a[i])
            
    s=0
    for i in range (0,n):
        s=s+i*rotated_a[i]

    return(rotated_a,s)

a=[3,2,1,4,12,23,11,25,34,5]
n=len(a)
s=[]

for i in range(n):
    res=Imultarray(a,n)
    a=res[0]
    s.append(res[1])
    print(res)

print('maximum summation is:', max(s)) 
    
 

