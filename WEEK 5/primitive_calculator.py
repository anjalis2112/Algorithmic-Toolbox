# Uses python3
import sys
import numpy as np
n=int(input())
min_count=[0]*(n+1) #minimum number of operations array init to 0
for i in range(2,n+1): #from 2 till n since 1 is known to be 0
    arr=[] #array to store the possible previous entry
    
    arr.append(i-1)

    if i%2==0:
        arr.append(i//2)
    if i%3==0:
        arr.append(i//3)
   
       

    min_c = min([min_count[x] for x in arr]) #find the minimum count amongst all 3 of them
    min_count[i]=min_c+1

tot=n
order=[]
order.append(n)
while tot!=1:
   
    minim=[]

    minim.append(tot-1)
    if tot%2==0:
        minim.append(tot//2)
    if tot%3==0:
        minim.append(tot//3)
    
   
    min_val=min([min_count[x] for x in minim])
    for p in minim:
        if min_count[p]==min_val:
            order.append(p)
            break
    tot=p


print(min_count[n])
for p in range(len(order)-1,-1,-1):
    print(order[p],end=" ")