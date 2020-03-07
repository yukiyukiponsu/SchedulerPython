import threading
import time

def count(cnt, sum):
    sum += cnt
    return sum

def scheduler(interval, wait = False):
    base_time = time.time()
    next_time = 0
    sum = 0
    cnt = 0
    while True:
        sum = count(cnt, sum)
        print(sum)
        cnt += 1
        #処理時間を考慮してSleepする時間を決定
        next_time = ((base_time - time.time()) % interval) or interval
        print(next_time)
        time.sleep(next_time)

scheduler(1, False)
