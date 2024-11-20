import time
import threading


def customer(id, arrive_time):
    global emptyChair, custOnChair
    time.sleep(arrive_time)
    mutex.acquire()
    if emptyChair > 0:
        print(f"customer {id}: there are {custOnChair} customers in front waiting for a haircut")
        emptyChair -= 1
        custOnChair += 1
        wait.release()
        mutex.release()
        barber.acquire()
        custOnChair -= 1
        emptyChair += 1
        time.sleep(t)
        mutex.acquire()
        print(f"customer {id} finished haircut")
        mutex.release()
    else:
        print(f"customer {id}: no more empty chairs, customer leaves")
        mutex.release()


def barber_thread():
    while True:
        wait.acquire()
        mutex.acquire()
        barber.release()
        mutex.release()
        time.sleep(t)


n, m, emptyChair, t = map(int, input().split())
custOnChair = 0
arrive_time = [None] * n
for i in range(n):
    j, k = map(int, input().split())
    arrive_time[j - 1] = k
mutex = threading.Semaphore(1)
wait = threading.Semaphore(0)
barber = threading.Semaphore(0)
barber_thread = threading.Thread(target=barber_thread)
barber_thread.daemon = True
barber_thread.start()
customer_threads = []
for i in range(n):
    customer_thread = threading.Thread(target=customer, args=(i + 1, arrive_time[i]))
    customer_threads.append(customer_thread)
    customer_thread.start()
for customer_thread in customer_threads:
    customer_thread.join()
