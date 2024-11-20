"""parent.py"""
import time
import os
import subprocess


def parent_process():
    while True:
        print(f"The parent is talking at {time.ctime()}")
        time.sleep(1)


if __name__ == "__main__":
    child_process = subprocess.Popen(["python3", "child.py"])
    parent_process()