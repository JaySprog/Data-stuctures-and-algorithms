import copy

def matrix_rotate(a):
    r=len(a)
    c=len(a[0]) 
    b=copy.deepcopy(a)
    
    for i in range(r):
        if i!=r-1:
            b[i][0]=a[i+1][0]
        if i!=0:
            b[i][c-1]=a[i-1][c-1]
        if i==0:
            for j in range(1,c):
                b[0][j]=a[0][j-1]
        if i==r-1:
            for j in range(0,c-1):
                b[r-1][j]=a[r-1][j+1]       
    return(b)  
          
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

res=matrix_rotate(a)
print(res)
      
