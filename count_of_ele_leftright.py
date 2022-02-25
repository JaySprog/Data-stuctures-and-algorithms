a=[2, 5, 1, 7, 3, 4, 0]
K=3

n=len(a)
b=[]

for i in range(0,n):
    ele=a[i]
    max_dec=ele
    for j in range(i-1,-1,-1):
        if a[j]> max_dec:
            b.append(max_dec)
            break
c=[]

for i in range (0,n):
    ele=a[i]
    K_check=[]
    for j in range (i+1,n,1):
        if ele>a[j]:
            K_check.append(a[j])

    
    if len(K_check)<K:
        c.append(ele)

d=set(a)-set(b+c)
print(d,len(d))
    


                            
    
    

 
