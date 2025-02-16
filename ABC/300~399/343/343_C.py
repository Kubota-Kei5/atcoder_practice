# %%
N = int(input())

for i in range(N, -1, -1): 
    cube_root = round(i ** (1/3))
    if cube_root ** 3 != i:
        continue
    
    if str(i) == str(i)[::-1]:
        print(i)
        exit()

# %%
N = int(input())

max_cube_root = N ** (1/3)

for cube_root in range(max_cube_root, 0, -1):
    cube = cube_root ** 3
    if cube != N:
        continue
    if str(int(cube)) == str(int(cube))[::-1]:
        print(int(cube))
        exit()
# %%
N = int(input())

max_cube_root = round(N ** (1/3))

for cube_root in range(max_cube_root, 0, -1):
    cube = cube_root ** 3
    if cube > N:
        continue
    if str(cube) == str(cube)[::-1]:
        print(cube)
        exit()
# %%
