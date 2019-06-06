# encoding=utf-8
"""
@author huxujun
@date 2019-06-03
"""
import json
import os


def object_to_json_file(obj: object, filename: str):
    file_dir = os.path.dirname(filename)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj.__dict__, f, ensure_ascii=False)


def json_file_to_object(obj: object, filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        obj.__dict__ = json.load(f)


if __name__ == '__main__':
    pass
