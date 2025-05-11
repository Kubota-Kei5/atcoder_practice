# %%

def print_pattern(n):
    if n < 2:
        print('#')
        return
    
    print('#' * n)
    
    for i in range(n - 2):
        row = ['#']
        
        for j in range(n - 2):
            layer = min(i, j, (n - 2 - 1 - i), (n - 2 - 1 - j))
            if layer % 2 == 0:
                row.append('.')
            else:
                row.append('#')
        
        row.append('#')
        print("".join(row))
    
    print('#' * n)

if __name__=="__main__":
    n=int(input())
    print_pattern(n)
# %%
