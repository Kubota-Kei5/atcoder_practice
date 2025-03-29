# %%
def main():
    import sys
    sys.setrecursionlimit(10**7)     # 再帰関数の再帰回数上限を指定
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]   # 隣接リストの初期化
    
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1  # 0-indexに変換
        v -= 1
        graph[u].append(v)
        graph[v].append(u)  # 無向グラフの初期状態を作成

    visited = [False] * N  # 各ノードの訪問状態を管理
    used_edges=set()  # 使用済みの辺を管理
    delete_edges = 0

    def dfs(v, parent):   # v：探索開始ノード, parent：親ノード
        nonlocal delete_edges
        visited[v] = True # 訪問済みの処理
        for neighbor in graph[v]:
            # 辺を一方向として扱い、重複カウントを防ぐ
            edge = tuple(sorted((v, neighbor)))
            if edge in used_edges:
                continue
            used_edges.add(edge)

            if not visited[neighbor]:
                dfs(neighbor, v)
            elif neighbor != parent:
                delete_edges += 1 #親以外の訪問済み => 閉路の検出

    for i in range(N):
        if not visited[i]: # 未訪問のノードがあればDFSを実行
            dfs(i, -1)

    # 無向グラフなので1つの閉路は2回数えられる => 半分にする
    print(delete_edges)

if __name__ == "__main__":
    main()

# %%
# これでAC
def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

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

    delete_count = 0
    for u, v in edges:
        u -= 1  # 0-index に変換
        v -= 1
        if not union(u, v):
            delete_count += 1

    print(delete_count)

if __name__ == "__main__":
    main()
