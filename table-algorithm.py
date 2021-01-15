from functools import lru_cache


@lru_cache(maxsize=5000)
def search(table, n, pre):
    if (table == 0) and (n == 0):
        # テーブル数と客数がともに0になれば終了
        return 1
    if (table <= 0) or (n <= 0) or (table * 2 < n):
        # いずれかが0になったり、テーブルの2倍を超えるとNG
        return 0

    cnt = 0
    for i in range(pre, n + 1):
        # 配置する人数(グループの人数)でチェック
        cnt += search(table - (i + 1) // 2, n - i, i)

    return cnt


# 最初はグループの人数を1人からスタート
print(search(50, 80, 1))