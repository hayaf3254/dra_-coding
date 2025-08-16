# longest_path_closer.py
import sys

graph = {}
nodes = set()

# 入力: "start, end, dist"
for line in sys.stdin:
    start, end, dist = line.strip().split(",")
    start = int(start)
    end = int(end)
    dist = float(dist)
    if start not in graph:
        graph[start] = []
    graph[start].append((end, dist))
    nodes.add(start)
    nodes.add(end)

# 出次数0のノードもキー化（for文で回せるように）
for v in nodes:
    if v not in graph:
        graph[v] = []

# visitedは「経路ごと」に使う（バックトラッキングで戻す）
visited = {node: False for node in nodes}

# 最長経路の記録
best_dist = float("-inf")
best_path = []

def dfs(current, path, total_dist):
    global best_dist, best_path

    visited[current] = True
    path.append(current)

    # ここで最長判定（ゴール固定しない）
    if total_dist > best_dist:
        best_dist = total_dist
        best_path = path.copy()

    # 次へ
    for nxt, dist in graph[current]:
        if not visited[nxt]:
            dfs(nxt, path, total_dist + dist)

    # バックトラッキング
    path.pop()
    visited[current] = False

# すべてのノードを始点として試す
for s in nodes:
    dfs(s, [], 0.0)

# 出力：最長経路に含まれる頂点IDを1行ずつ
for v in best_path:
    print(v)
