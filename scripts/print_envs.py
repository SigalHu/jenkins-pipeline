# encoding=utf-8
"""
@author huxujun
@date 2019-05-31
"""
import os


def print_envs():
    print("message1=%s" % os.getenv("message1"))
    print("message2=%s" % os.getenv("message2"))
    print("PYTHONPATH=%s" % os.getenv("PYTHONPATH"))

    print("Start to print all env...")
    for k, v in os.environ.items():
        print(k + "=" + v)
    print("end.")


if __name__ == '__main__':
    print_envs()
