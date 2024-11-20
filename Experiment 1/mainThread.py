"""mainThread.py"""
import time
import threading


def child_thread():
    while True:
        print(f"Child Thread ID: {threading.get_ident()} {time.ctime()}")
        time.sleep(1)


def main_thread():
    while True:
        print(f"Main Thread ID: {threading.get_ident()} {time.ctime()}")
        time.sleep(1)


if __name__ == "__main__":
    child = threading.Thread(target=child_thread)
    child.start()
    main_thread()
