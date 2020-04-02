# Uses python3
import sys
import numpy as np 

money=int(input())
coin=np.array([1,3,4])
min_coin= np.zeros(money+1,dtype=np.int64)
min_coin[0]=0
for i in range(1,money+1):
    min_coin[i]=99999
    for j in coin:
        if i>=j:
            num_coin=min_coin[i-j]+1
            if num_coin<min_coin[i]:
                min_coin[i]=num_coin

print(min_coin[money])   



