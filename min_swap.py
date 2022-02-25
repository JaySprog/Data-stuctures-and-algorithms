a = [1, 12, 10, 3, 14, 8,9,10,12,13,14,15,7,8,9,22,23,21,10,15,21,12,33,11,56, 5,4,5,7,5,1,0,12,34,5,3,7]
k=14
count_number=0
b=[]
for i in a:
    if i<=k:
        count_number=count_number+1
        b.append(i)
print('total elements equal/smaller than k:', count_number)

sub_array=[]
for i in range(count_number):
    sub_array.append(0)

count_array=[]
for i in range (len(a)-count_number+1):
    for j in range(i,count_number+i):
        sub_array[j-i]=a[j]

    print('sub_array:',sub_array)

    count=0
    for r in range (count_number):
        if sub_array[r]>k:
            count=count+1

    print('count of greater elements thank k is:',count)            
    count_array.append(count)

min_swap=min(count_array)
print('min_swap=',min_swap)
 
