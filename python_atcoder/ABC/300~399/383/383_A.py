tl = []
vl = []
N = int(input())
for i in range(N):
    t, v = map(int, input().split(" "))
    tl.append(t)
    vl.append(v)

A = vl[0]

for i in range(1,N):
    if A-(tl[i]-tl[i-1])<=0:
        A = vl[i]
    else:
        A = A-(tl[i]-tl[i-1])+vl[i]
print(A)