#python3
d=int(input()) #distance
m=int(input()) #maxm distance that can be travelled on full tank
n=int(input()) #no of stations

arr = list(map(int, input().split()))
arr.insert(0,0)
arr.insert(n+1,d)
curr=0
num=0
z=0
while(curr<=n):
    last=curr
    while(curr<=n and arr[curr+1]-arr[last]<=m):
        curr=curr+1
        
    
    if(curr==last):
        z=-1
        break
            
    if(curr<=n):
        num+=1

if(z==-1):
    print(-1)

elif(d<m):
    print(0)

else:
    print(num)
        

    
    
    