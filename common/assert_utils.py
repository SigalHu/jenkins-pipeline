# encoding=utf-8
"""
@author huxujun
@date 2019-06-14
"""
from common import net_utils


def valid_port(host: str, port: int):
    assert port, "The port {}:{} is invalid!".format(host, port)
    is_connect, ex = net_utils.ping(host, port)
    assert not is_connect, "The port {}:{} already be in use!".format(host, port)


def port_in_use(host: str, port: int):
    assert port, "The port {}:{} is invalid!".format(host, port)
    is_connect, ex = net_utils.ping(host, port)
    assert is_connect, "The port {}:{} must be in use!".format(host, port)


def all_not_empty(**kwargs):
    empty_list = [k for k, v in kwargs.items() if not v]
    assert not empty_list, "The {} must be not empty!".format(empty_list)


if __name__ == '__main__':
    pass
