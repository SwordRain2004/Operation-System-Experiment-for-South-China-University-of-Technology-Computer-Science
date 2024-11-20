import time
import threading


def reader(id, arrive_time, consume_time):
    global reader_count, waiting_writers
    time.sleep(arrive_time)
    mutex.acquire()
    print(f"reader {id} waiting to read")
    reader_count += 1
    if reader_count == 1:
        rwlock.acquire()
    mutex.release()
    print(f"reader {id} starts to read")
    time.sleep(consume_time)
    print(f"reader {id} ends reading")
    mutex.acquire()
    reader_count -= 1
    if reader_count == 0:
        rwlock.release()
    mutex.release()


def writer(id, arrive_time, consume_time):
    global waiting_writers
    time.sleep(arrive_time)
    print(f"writer {id} waiting to write")
    if priority == 1:
        mutex.acquire()
        waiting_writers += 1
        mutex.release()
    rwlock.acquire()
    print(f"writer {id} starts to write")
    time.sleep(consume_time)
    print(f"writer {id} ends writing")
    rwlock.release()
    if priority == 1:
        mutex.acquire()
        waiting_writers -= 1
        mutex.release()


priority, n = map(int, input().split())
info = [None] * n
for _ in range(n):
    number, action, arrive_time, consume_time = input().split()
    number = int(number)
    arrive_time = int(arrive_time)
    consume_time = int(consume_time)
    info[number - 1] = (action, arrive_time, consume_time)
mutex = threading.Semaphore(1)
wmutex = threading.Semaphore(1)
reader_count = 0
read_wait = threading.Semaphore(0)
write_wait = threading.Semaphore(0)
rwlock = threading.Semaphore(1)
waiting_writers = 0
threads = []
for i, (action, arrive_time, consume_time) in enumerate(info):
    if action == 'R':
        t = threading.Thread(target=reader, args=(i + 1, arrive_time, consume_time))
    else:
        t = threading.Thread(target=writer, args=(i + 1, arrive_time, consume_time))
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()