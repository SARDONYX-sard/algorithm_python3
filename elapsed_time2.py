# 時間計測用デコレーター
from functools import wraps
import time

"""
「経過時間を表示」
計測したい関数の上に@elapsed_time()と記述

・digit仮引数に小数点以下の有効桁数を指定可能。default = 2
・time仮引数には試行回数を指定可能。default = 1
・timeが2以上なら平均試行時間を自動表示。


[小数点以下5桁」、「試行回数3回」の例：
from elapsed_time2 import elapsed_time2

@elapsed_time(digit=5, t=3)
def main():
    pass
"""


def elapsed_time(digit=3, t=1):
    def _elapsed_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed_times = 0
            for _ in range(t):
                start = time.time()
                func(*args, **kwargs)
                elapsed_time_ = time.time() - start
                elapsed_times += elapsed_time_
                print(f'elapsed_time:{elapsed_time_:.{digit}f}[sec]')

            if t >= 2:
                mean = elapsed_times / t
                print(f'mean_elapsed_time:{mean:.{digit}f}[sec]')

        return wrapper

    if t <= 0:
        print("@elapsed_time's times<=0 is fixed to 1.")
        t = 1
    return _elapsed_time
