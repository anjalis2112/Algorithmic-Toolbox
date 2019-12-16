#python3
n, w = [int(x) for x in input().split()]
value= []
weight=[]

for i in range(n):
    v,we= [int(x) for x in input().split()]
    value.append(v)
    weight.append(we)

price=[]
for j in range(n):
    price.append(value[j]/weight[j])


i=0

for i in range(n):
        for k in range(0, n-i-1):
            if price[k]<price[k+1] :
                price[k], price[k+1] = price[k+1], price[k]
                weight[k], weight[k+1] = weight[k+1], weight[k]
                value[k], value[k+1] = value[k+1], value[k]


i=0
final=0
for i in range(n):
    if(w==0):
        break
    
    if(weight[i]<=w and weight[i]>0):
        final+=weight[i]*price[i]
        w-=weight[i]
        weight[i]=0
       
    
    else:
        weight[i]-=weight[i]-w
        final+=w*price[i]
        w=0
        
print ('%.4f'%final)
     
               
           
