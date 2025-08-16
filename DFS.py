import sys

graph = {}

for line in sys.stdin:
    start, end, dist = line.strip().split(",")  # カンマで分割
    start = int(start)
    end = int(end)
    dist = float(dist)

    if start not in graph:
        graph[start] = []
    graph[start].append((end, dist))

visited = {node: False for node in graph}

# ゴール
goal = 4

def dfs(current, path, total_dist):
    visited[current] = True
    path.append(current)

    if current == goal:
        print(path, total_dist)  # 経路と距離を出力
        return path,total_dist
    else:
        for nxt, dist in graph[current]:
            print(graph[current])
            if not visited[nxt]:
                print(nxt,path,dist)
                dfs(nxt, path, total_dist + dist)

    # バックトラッキング
    path.pop()
    visited[current] = False

# スタートは1
result = dfs(1, [], 0.0)
if result:
    path, total_dist = result
    print(path, total_dist)