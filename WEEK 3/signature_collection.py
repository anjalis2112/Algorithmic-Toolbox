#python3
def sorting(last,first):
    for i in range(n):
            for k in range(0, n-i-1):
                if last[k]>last[k+1] :
                    last[k], last[k+1] = last[k+1], last[k]
                    first[k], first[k+1] = first[k+1], first[k]



n=int(input())
first= []
last=[]

for i in range(n):
    f,l= [int(x) for x in input().split()]
    first.append(f)
    last.append(l)
points=[]
j=0
sorting(last,first)
while(len(last)>0):
   
    minim=last[0]
    points.append(minim)
    while(j<len(last)):
        if(minim>=first[j] and minim<=last[j]):
            
            del first[j]
            del last[j]
        else:
            break

print(len(points))
for z in range(len(points)):
    print(points[z], end =" ")