# coding: utf-8
#
# pqueue.py : 優先度つき待ち行列
#
#
from elapsed_time2 import elapsed_time


# 葉の方向へ
def _down_heap(buff, n):
    size = len(buff)
    while True:
        c = 2 * n + 1
        if c >= size:
            break
        if c + 1 < size:
            if buff[c] > buff[c + 1]:
                c += 1
        if buff[n] <= buff[c]:
            break
        temp = buff[n]
        buff[n] = buff[c]
        buff[c] = temp
        n = c


# 根の方向へ
def _up_heap(buff, n):
    while True:
        p = (n - 1) // 2
        if p < 0 or buff[p] <= buff[n]:
            break
        temp = buff[n]
        buff[n] = buff[p]
        buff[p] = temp
        n = p


class PQueue:
    def __init__(self, buff=None):
        if buff is None:
            buff = []
        self.buff = buff[:]  # コピー
        for n in range(len(self.buff) // 2 - 1, -1, -1):
            _down_heap(self.buff, n)

    # データの追加
    def push(self, data):
        self.buff.append(data)
        _up_heap(self.buff, len(self.buff) - 1)

    # 最小値を取り出す
    def pop(self):
        if len(self.buff) == 0:
            raise IndexError
        value = self.buff[0]
        last = self.buff.pop()
        if len(self.buff) > 0:
            # ヒープの再構築
            self.buff[0] = last
            _down_heap(self.buff, 0)
        return value

    # 最小値を求める
    def peek(self):
        if len(self.buff) == 0:
            raise IndexError
        return self.buff[0]

    # 空か
    def is_empty(self):
        return len(self.buff) == 0


# テスト
@elapsed_time(digit=5, t=4)
def main():
    import random
    a = PQueue()
    for x in range(10):
        n = random.randint(0, 100)
        a.push(n)
        print(n, 'min data = ', a.peek())
    while not a.is_empty():
        print(a.pop(), end=", ")
    print()
    data = [random.randint(0, 100) for _ in range(10)]
    print(data)
    a = PQueue(data)
    while not a.is_empty():
        print(a.pop(), end=", ")
    print()


if __name__ == '__main__':
    main()
