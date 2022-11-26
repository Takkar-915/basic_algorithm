# bit全探索
# 与えられた全パターンがbit(0 or 1)の組み合わせで表現できる場合に、それらの組み合わせをすべて列挙できる
# ただしO(2^n)なので計算量がすぐに大変なことになりそう…

# 部分和問題

from itertools import product


def judge(pro):
    sum = 0
    for i in range(N):
        if pro[i]:
            sum += A[i]
    if sum == W:
        return 1
    else:
        return 0


N, W = map(int, input().split())

A = list(map(int, input().split()))

ans = 0

for pro in product((0, 1), repeat=N):
    ans += judge(pro)
print(ans)
