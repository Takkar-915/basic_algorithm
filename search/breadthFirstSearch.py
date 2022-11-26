# 幅優先探索(BFS)

# 探索途中のノードをキューに保存しておく必要がある
# メモリの使用量は深さ優先探索よりも増える
# depueを使用すればO(1)で処理ができる

# 出題例(https://atcoder.jp/contests/atc002/tasks/abc007_3)

from collections import deque

R, C = map(int, input().split())

sx, sy = map(int, input().split())

gx, gy = map(int, input().split())

maze = [list(input()) for _ in range(R)]

# スタート、ゴールの座標をリストのインデックスに対応させる
sx -= 1
sy -= 1
gx -= 1
gy -= 1

# 最小手数を管理    (十分に大きい値で初期化)
dist = [[10**4 for _ in range(C)] for _ in range(R)]

# スタート地点の最小手数を0とする。
dist[sx][sy] = 0

que = deque()
que.append([sx, sy])

# 移動方向のリスト
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 幅優先探索
while que:
    x, y = que.popleft()

    for i, j in d:
        # 範囲外
        if x+i >= R or x+i < 0 or y+j >= C or y-j < 0:
            continue

        # 障害物
        if maze[x+i][y+j] == "#":
            continue

        # 既に探索済
        if dist[x+i][y+j] != 10 ** 4:
            continue
        dist[x+i][y+1] = dist[x][y] + 1

        que.append([x+i, y+j])

print(dist[gx][gy])
