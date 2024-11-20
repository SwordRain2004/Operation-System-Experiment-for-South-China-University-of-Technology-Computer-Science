import os
import fnmatch
import time
import argparse


# 检查文件是否符合修改时间条件
def match_mtime(filepath, days):
    try:
        file_mtime = os.path.getmtime(filepath)
        current_time = time.time()
        file_days = (current_time - file_mtime) // (60 * 60 * 24)
        return file_days == days
    except Exception as e:
        print(f"无法获取文件修改时间: {filepath}, 错误: {e}")
        return False


# 递归搜索目录
def search_dir(path, name_pattern=None, mtime_days=None):
    try:
        for root, dirs, files in os.walk(path):
            for filename in files:
                filepath = os.path.join(root, filename)
                if name_pattern and not fnmatch.fnmatch(filename, name_pattern):
                    continue
                if mtime_days is not None and not match_mtime(filepath, mtime_days):
                    continue
                print(filepath)
    except Exception as e:
        print(f"无法访问目录: {path}, 错误: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-name")
    parser.add_argument("-mtime", type=int)
    args = parser.parse_args()
    search_dir(args.path, name_pattern=args.name, mtime_days=args.mtime)


if __name__ == "__main__":
    main()
