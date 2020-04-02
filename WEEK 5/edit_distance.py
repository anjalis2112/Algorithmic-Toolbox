# Uses python3
import numpy as np
str1=input()
str2=input()

if str1==str2:
    print(0)
    exit()
edit_dist=0
len1=len(str1)+1
len2=len(str2)+1
arr=np.zeros((len1,len2), dtype='int32')

for i in range(1,len2):
    arr[0][i]=i
for i in range(1,len1):
    arr[i][0]=i
for i in range(1,len1):
    for j in range(1,len2):
        insertion=arr[i-1][j]+1
        deletion=arr[i][j-1]+1
        match=arr[i-1][j-1]
        mismatch=arr[i-1][j-1]+1
        if(str1[i-1]==str2[j-1]):
            arr[i][j]=min(insertion,deletion,match)
        else:
            arr[i][j]=min(insertion,deletion,mismatch)

print(arr[len1-1][len2-1])
