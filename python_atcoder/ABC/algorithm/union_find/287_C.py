# https://atcoder.jp/contests/abc287/tasks/abc287_c

# %%
def main():
    import sys
    sys.setrecursionlimit(10**7)

    N, M = map(int, input().split())
    edges=[]
    for i in range(M):
        u,v = map(int, input().split())
        if u > v:
            u,v = v,u
        edges.append((u,v))
    
    
    # Union-Find構造
    parent = list(range(N))
    size = [1] * N

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # 経路圧縮
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False  # 閉路発見 → 削除すべき辺
        
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        size[rx] += size[ry]
        return True

    for u, v in edges:
        u -= 1  # 0-index に変換
        v -= 1
        if not union(u, v):
            print('No')
            return

    # rootノードが1つか確認
    root_count = sum(1 for i in range(N) if find(i) == i)
    if root_count != 1:
        print('No')
        return

    # 辺の数がノードの数-1になっているか確認
    if M != N - 1:
        print('No')
        return

    print('Yes')
    
if __name__ == "__main__":
    main()
