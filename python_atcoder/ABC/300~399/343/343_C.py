N = int(input())
max_cube_root = round(N ** (1/3))

for cube_root in range(max_cube_root, 0, -1):
    cube = cube_root ** 3
    if cube > N:
        continue
    if str(cube) == str(cube)[::-1]:
        print(cube)
        exit()