"""shareVar.py"""
import time
import threading

shared_var = 0
lock = threading.Lock()


def child_thread():
    global shared_var
    while True:
        with lock:
            shared_var -= 1
        print(f"Shared Var in Child Thread: {shared_var}, sleep for 1 second")
        time.sleep(1)


def main_thread():
    global shared_var
    while True:
        with lock:
            shared_var += 1
        print(f"Shared Var in Main Thread: {shared_var}, sleep for 1 second")
        time.sleep(1)


if __name__ == "__main__":
    child = threading.Thread(target=child_thread)
    child.start()
    main_thread()
