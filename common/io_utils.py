# encoding=utf-8
"""
@author huxujun
@date 2019-06-17
"""
import logging
import os


def load_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        logging.exception("Error to read file %s", filename)


def save_file(filename, content=""):
    try:
        filedir = os.path.dirname(filename)
        if filedir and not os.path.exists(filedir):
            os.makedirs(filedir)
        with open(filename, "w") as f:
            f.write(content)
    except:
        logging.exception("Error to write file %s", filename)


if __name__ == '__main__':
    pass
