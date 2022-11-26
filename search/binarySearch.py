# 2分探索
# ソートされていれば適用可能

import random
import time


def binarySearch(searchList, target):
    low = 0
    high = len(searchList)-1

    while high >= low:
        mid = (high + low) // 2
        if target == mid:
            return mid
        elif target > mid:
            low = mid + 1
        elif target < mid:
            high = mid - 1


searchList = [i for i in range(1000)]
searchList.sort()

# 探索対象の設定
target = random.randint(0, 1000)


# 探索と実行時間の計測
start_time = time.perf_counter()

ans = binarySearch(searchList, target)

end_time = time.perf_counter()

print(ans)

elapsed_time = end_time - start_time
print(elapsed_time)
