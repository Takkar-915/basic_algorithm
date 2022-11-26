# defaultdict

# 特定の値のアクセスに、listならo(n)の計算量を要するが、dictならo(1)でアクセスできる
# defaultdict型は、変数としてはdict型ではあるが、デフォルトのvalue値のオブジェクトが指定されたオブジェクトになる

from collections import defaultdict

cnt_alpha = {}
cnt_alpha = defaultdict(int)
alpha = ['A', 'D', 'A', 'C', 'H', 'I', 'T', 'O',
         'S', 'H', 'I', 'M', 'A', 'M', 'U', 'R', 'A']

for key in alpha:
    cnt_alpha[key] += 1
print(cnt_alpha)
