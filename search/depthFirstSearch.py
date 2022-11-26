# 深さ優先探索(DFS)

# 現在のノード情報しか持たないので、メモリの使用量は少ない
# 最短経路を1つ見つけ出す場合は、BFSの方が処理が速い

# 出題例(https://atcoder.jp/contests/atc001/tasks/dfs_a)

import sys


def dfs(x, y):
    # 範囲外、もしくは壁の場合は終了
    if x >= H or x < 0 or y >= W or y < 0 or maze[x][y] == "#":
        return

    # ゴールにたどり着いたら終了
    if maze[x][y] == "g":
        print("Yes")
        sys.exit()

    # 確認したルートは壁にする
    maze[x][y] = "#"

    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)


# 再帰関数の呼び出し上限(デフォルトは1000)
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())

maze = [list(input()) for _ in range(H)]

# スタート地点の設定
for h in range(H):
    for w in range(W):
        if maze[h][w] == "s":
            sx, sy = h, w

dfs(sx, sy)
print("No")
