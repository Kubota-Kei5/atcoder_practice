# %%
N, D = map(int, input().split())
T=[]
L=[]
for i in range(N):
    t,l=map(int,input().split())
    T.append(t)
    L.append(l)

S = []
for j in range(N):
    S.append(T[j]*L[j])

A=[]
M=[]
for k in range(1,D+1):
    for p in range(N):
        a=S[p]+T[p]*k
        A.append(a)
    m=max(A)
    M.append(m)
    A=[]

for q in range(D):
    print(M[q])

# %%
