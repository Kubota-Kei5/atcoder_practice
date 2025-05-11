N=int(input())
l=list(map(int,input().split()))
cnt=0
ans=0

def count_element(list,N):
    element=0
    for i in range(N):
        if list[i]>=1:
            element+=1
    return element

while cnt<=1:
    ans+=1
    l.sort(reverse=True)
    l[0],l[1] = l[0]-1,l[1]-1
    if count_element(l,N)<=1:
        break        

print(ans)