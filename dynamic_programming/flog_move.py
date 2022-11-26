# 動的計画法
# 小さい問題の結果を利用して解くアルゴリズム
# 例題1 (https://gihyo.jp/book/2022/978-4-297-12521-9)

N = int(input())
H = list(map(int, input().split()))

dp = [0 for _ in range(N)]

dp[0] = 0
dp[1] = abs(H[1]-H[0])

for i in range(2, N):
    dp[i] = min(dp[i-1]+abs(H[i] - H[i-1]), dp[i-2] + abs(H[i] - H[i-2]))

ans = dp[N-1]
print(ans)
