# 時間計測用デコレーター
from functools import wraps
import time

"""
「経過時間を表示」
計測したい関数の上に@elapsed_timeと記述

例：
from elapsed_time import elapsed_time

@elapsed_time
def main():
    pass
"""


def elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        elapsed_time_ = time.time() - start
        print(f'elapsed_time:{elapsed_time_}[sec]')

    return wrapper
