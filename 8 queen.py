# encoding utf-8
#
# 8クイーン問題
# リスト内が行、インデックスが列を表す

from elapsed_time import elapsed_time


class Queen8:
    def __init__(self, queen_num):
        self.board = []
        self.count = 0
        self.n = queen_num

    # クイーン同士が斜めで衝突していないか検証
    def check(self, n):
        for y in range(1, n):  # クイーンの個数 - 1回
            if self.conflict(self.board[y], y):  # 横、縦（インデックス）
                return False  # 衝突していたらFalse(検証は不合格)を返す
        return True

    # 斜め衝突判定をbool型で返す
    def conflict(self, x, y):
        for y1 in range(0, y):
            x1 = self.board[y1]  # y1列目のリストの値をx1へ。
            if x1 - y1 == x - y or x1 + y1 == x + y:
                return True  # 衝突していたらTrue(衝突している)を返す
        return False

    # 愚直な総当たり
    def queen(self, y=0):
        if self.n == y:  # クイーンをすべて配置したか判定,
            if self.check(self.n):  # 斜めの衝突検証に合格したら,
                print(self.board)  # ボードを出力
                self.count += 1
        else:
            for x in range(0, self.n):  # クイーンの個数 + 1 回繰り返す
                if x in self.board:  # 一つずつ行の衝突判定
                    continue  # 同じ行にクイーンがあったら下の処理はせずfor文へ戻る
                self.board.append(x)  # 行の衝突がなかったら、ボードにクイーンを仮に置いてみる
                self.queen(y + 1)  # １つ次の列についても再帰で検証
                self.board.pop()  # 次の列にどこにも置けなかったら仮に置いたクイーンを取り除く

    # より無駄のない列挙
    def fast_queen(self, y=0):
        if self.n == y:
            print(self.board)
            self.count += 1
        else:
            for x in range(0, self.n):
                if x in self.board or self.conflict(x, y):  # 全方向の衝突検証をこの時点で実行
                    continue
                self.board.append(x)
                self.fast_queen(y + 1)
                self.board.pop()


@elapsed_time
def main():
    buff = Queen8(8)  # buffは一時メモリ「バッファ」の意味でよく名付けられる
    buff.fast_queen()
    # buff.queen()


if __name__ == '__main__':
    main()
