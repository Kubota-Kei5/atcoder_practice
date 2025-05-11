N = str(input())
a=N[0]
b=N[1]
c=N[2]

X = 100*int(b) + 10*int(c) + int(a)
Y = 100*int(c) + 10*int(a) + int(b)

print(f'{X} {Y}')