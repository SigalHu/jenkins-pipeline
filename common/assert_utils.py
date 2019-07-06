# encoding=utf-8
"""
@author huxujun
@date 2019-06-14
"""


def all_not_empty(**kwargs):
    empty_list = [k for k, v in kwargs.items() if not v]
    assert not empty_list, "The {} must be not empty!".format(empty_list)


if __name__ == '__main__':
    pass
